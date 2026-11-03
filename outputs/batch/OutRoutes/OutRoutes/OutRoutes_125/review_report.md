# Play-Annotation-Generator Annotation Review — OutRoutes_125

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_125`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 48
- **Validation Warnings:** 48
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 25
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_RunOutRoute` | WR4 | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_SecureCatch` | WR4 | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR4 | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `12` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `6` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_PassBlock` | C | `14` | `14` | 15 | START | 15 | 117 |
| ✅ EXACT | `Action_PassBlock` | LG | `18` | `18` | 15 | START | 15 | 138 |
| ✅ EXACT | `Action_PassBlock` | LT | `19` | `19` | 15 | START | 15 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 15 | START | 15 | 56 |
| ✅ EXACT | `Action_PassBlock` | RT | `9` | `9` | 15 | START | 15 | 68 |
| ✅ EXACT | `Action_RunOutRoute` | WR4 | `6` | `6` | 20 | START | 20 | 86 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 20 | END | 20 | 20 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 57 | START | 57 | 65 |
| ✅ EXACT | `Action_SecureCatch` | WR4 | `6` | `6` | 87 | START | 87 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR4 | `6` | `6` | 96 | START | 96 | 128 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 20 | 1 | inferred_complete_timeline |
| `Action_None` | 21 | 56 | 36 | inferred_complete_timeline |
| `Action_ThrowPass` | 57 | 65 | 9 | inferred_complete_timeline |
| `Action_None` | 66 | 113 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_RunOutRoute` | 20 | 86 | 67 | inferred_complete_timeline |
| `Action_SecureCatch` | 87 | 95 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 96 | 128 | 33 | inferred_complete_timeline |
| `Action_BallCarry` | 130 | 161 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 77 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 85 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 180 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 105 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 138 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 117 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 56 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 58 | 119 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 68 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 115 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 93 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 111 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

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
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 180 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 169 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 174 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

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
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
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
| `21` | `21` | Position_Unknown | Team_Unknown | 0–102 | 103 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 67–70 | 4 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 80–81 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 96–117 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 36 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 132: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 132: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-93] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-111] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-115] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [96-128] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [130-161] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-159] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-85] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-113] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-138] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-105] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-56] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [58-119] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-70] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-117] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.

</details>