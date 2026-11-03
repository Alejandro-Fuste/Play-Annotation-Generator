# Play-Annotation-Generator Annotation Review — OutRoutes_91

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_91`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 60
- **Validation Warnings:** 54
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 38
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `5` | `5` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `0` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `12` | `12` | 15 | START | 15 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `15` | `15` | 15 | START | 15 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `17` | `17` | 15 | START | 15 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 15 | START | 15 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 15 | START | 15 | 20 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `5` | `5` | 20 | START | 20 | 91 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 20 | END | 20 | 20 |
| ✅ EXACT | `Action_ThrowPass` | QB | `11` | `11` | 59 | START | 59 | 69 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `5` | `5` | 92 | START | 92 | 106 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `5` | `5` | 107 | START | 107 | 141 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 20 | 1 | inferred_complete_timeline |
| `Action_None` | 21 | 58 | 38 | inferred_complete_timeline |
| `Action_ThrowPass` | 59 | 69 | 11 | inferred_complete_timeline |
| `Action_None` | 70 | 81 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_RunOutRoute` | 20 | 91 | 72 | inferred_complete_timeline |
| `Action_SecureCatch` | 92 | 106 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 107 | 141 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 134 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `0`</summary>

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
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 78 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 114 | 150 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 64 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 78 | 81 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 88 | 93 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 150 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 86 | 72 | inferred_complete_timeline |
| `Action_PassBlock` | 88 | 93 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 108 | 150 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–39
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 20 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 39 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 20 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 84 | 63 | inferred_complete_timeline |
| `Action_PassBlock` | 88 | 93 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 114 | 146 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 150 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 86 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 93 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 150 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 82 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 148 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 84 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 93 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 150 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

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
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 100 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 150 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 112–150 | 39 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 125–150 | 26 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 2 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 2 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 4 |
| Missing visible bounding boxes during action | 48 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-134] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [107-141] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-143] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-90] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-148] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-78] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [114-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-93] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-64] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [78-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [83-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [88-93] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-20] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [88-93] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [114-146] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-84] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-93] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-86] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [88-93] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [108-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-20] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-39] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.

</details>