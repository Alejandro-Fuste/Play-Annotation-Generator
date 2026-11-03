# Play-Annotation-Generator Annotation Review — OutRoutes_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_1`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 58
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 37
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `14` | `14` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | offense | `19` | `19` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `10` | `10` |
| ✅ EXACT | `Action_SecureCatch` | WR3 | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `15` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `19` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_PassBlock` | RT | `14` | `14` | 12 | START | 12 | 150 |
| ✅ EXACT | `Action_PassBlock` | LG | `16` | `16` | 12 | START | 12 | 150 |
| ✅ EXACT | `Action_PassBlock` | C | `20` | `20` | 12 | START | 12 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 12 | START | 12 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `4` | `4` | 12 | START | 12 | 109 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 14 | END | 14 | 14 |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | `19` | `19` | 16 | START | 16 | 88 |
| ✅ EXACT | `Action_ThrowPass` | RB | `10` | `10` | 55 | START | 55 | 65 |
| ✅ EXACT | `Action_SecureCatch` | WR3 | `19` | `19` | 89 | START | 89 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `19` | `19` | 91 | START | 91 | 130 |

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
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_SnapReceive` | 14 | 14 | 1 | inferred_complete_timeline |
| `Action_None` | 15 | 150 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ThrowPass` | 55 | 65 | 11 | inferred_complete_timeline |
| `Action_None` | 66 | 150 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_RunOutRoute` | 16 | 88 | 73 | inferred_complete_timeline |
| `Action_SecureCatch` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 91 | 130 | 40 | inferred_complete_timeline |
| `Action_BallCarry` | 146 | 147 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 150 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 109 | 98 | inferred_complete_timeline |
| `Action_PassBlock` | 113 | 150 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 150 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 150 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 30 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 34 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 150 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 150 | 139 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 78 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 150 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 150 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 140 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 150 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–150 | 151 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 29–81 | 19 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 29–47 | 17 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 48–50 | 3 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 70–79 | 8 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 114–150 | 35 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 120–150 | 30 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 147–149 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 4: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-71] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-78] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-109] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [113-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-135] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-140] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-150] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-150] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [91-130] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [146-147] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-30] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-34] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-31] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-70] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-81] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-36] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-47] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-50] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-72] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-79] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-115] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-150] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-134] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>