# Play-Annotation-Generator Annotation Review — Slants0to10_39

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_39`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 70
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_RunSlantRoute` | WR1 | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 2 |
| ✅ EXACT | `Action_PassBlock` | RG | `16` | `16` | 3 | START | 3 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 3 | START | 3 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `19` | `19` | 3 | START | 3 | 92 |
| ✅ EXACT | `Action_PassBlock` | C | `20` | `20` | 3 | START | 3 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `9` | `9` | 3 | START | 3 | 97 |
| ✅ EXACT | `Action_RunSlantRoute` | WR1 | `5` | `5` | 15 | START | 15 | 60 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 15 | END | 15 | 15 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 41 | START | 41 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `5` | `5` | 78 | START | 78 | 162 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_SnapReceive` | 15 | 15 | 1 | inferred_complete_timeline |
| `Action_None` | 16 | 40 | 25 | inferred_complete_timeline |
| `Action_ThrowPass` | 41 | 51 | 11 | inferred_complete_timeline |
| `Action_None` | 52 | 180 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 15 | 60 | 46 | inferred_complete_timeline |
| `Action_None` | 61 | 77 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 78 | 162 | 85 | inferred_complete_timeline |
| `Action_BallCarry` | 165 | 166 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 92 | 90 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 161 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 59 | 57 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 69 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 72 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–29
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 29 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 180 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 97 | 95 | inferred_complete_timeline |
| `Action_PassBlock` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 107 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 38 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 179 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 78 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 115 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 163 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 42 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 63 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 75 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 140 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 145 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–180 | 176 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 53–180 | 120 | 5 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 63–180 | 116 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 84–180 | 41 | 5 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 87–180 | 94 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 97–180 | 84 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 99–157 | 59 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 2 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 40: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ Row 40: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-38] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-47] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-179] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [78-162] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [165-166] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-159] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-78] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-115] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-163] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-101] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-97] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [99-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-135] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-140] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-59] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-72] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-92] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-161] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-29] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-42] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-63] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-75] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-61] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-64] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-81] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-64] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-90] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-101] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-170] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-157] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>