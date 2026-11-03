# Play-Annotation-Generator Annotation Review — OutRoutes_6

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_6`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 60
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_RunOutRoute` | TE | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `3` |
| ✅ EXACT | `Action_ThrowPass` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 40 |
| ✅ EXACT | `Action_PassBlock` | RT | `1` | `1` | 15 | START | 15 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `11` | `11` | 15 | START | 15 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `13` | `13` | 15 | START | 15 | 16 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `5` | `5` | 15 | START | 15 | 105 |
| ✅ EXACT | `Action_RunOutRoute` | TE | `12` | `12` | 24 | START | 24 | 70 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `3` | 24 | END | 24 | 24 |
| ✅ EXACT | `Action_ThrowPass` | RG | `13` | `13` | 55 | START | 55 | 68 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `21` | `20` | 91 | START | 91 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `21` | `20` | 95 | START | 95 | 155 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 24 | 1 | inferred_complete_timeline |
| `Action_None` | 25 | 45 | 21 | inferred_complete_timeline |
| `Action_None` | 47 | 88 | 42 | inferred_complete_timeline |
| `Action_None` | 91 | 100 | 10 | inferred_complete_timeline |
| `Action_None` | 105 | 118 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_RunOutRoute` | 24 | 70 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 78 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 136 | 53 | inferred_complete_timeline |
| `Action_PassBlock` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 159 | 169 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 105 | 91 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 127 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 16 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 39 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 54 | 14 | inferred_complete_timeline |
| `Action_ThrowPass` | 55 | 68 | 14 | inferred_complete_timeline |
| `Action_None` | 69 | 125 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 105 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 81 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 157 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 180 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 157 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
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
| `14` | `14` | Position_Unknown | Team_Unknown | 18–24 | 7 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 32–117 | 86 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 53–111 | 54 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 58–106 | 26 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 65–125 | 61 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 73–180 | 108 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 75–180 | 101 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 87–117 | 31 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 135–180 | 40 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 155–180 | 26 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 163–170 | 8 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 167–180 | 11 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 49 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-157] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-105] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-45] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-88] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-100] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-81] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-105] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-127] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-145] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-157] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-180] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-138] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-78] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-136] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [143-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [156-157] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [159-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [24-70] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-16] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-39] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-125] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-24] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-117] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-111] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-65] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-125] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [95-155] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [161-180] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-117] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-148] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-180] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-170] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-169] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-180] for track '25' has 2 frames without a visible bounding box.
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

</details>