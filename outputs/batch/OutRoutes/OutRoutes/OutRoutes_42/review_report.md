# Play-Annotation-Generator Annotation Review — OutRoutes_42

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_42`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 53
- **Validation Warnings:** 70
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 33
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `1` | `1` |
| ⚠️ START CHANGED | `Action_PassBlock` | RG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `13` | `13` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `5` | `5` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | LB1 | defense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_SecureCatch` | LB1 | defense | `6` | `6` |
| ✅ EXACT | `Action_BallCarry` | LB1 | defense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 30 |
| ✅ EXACT | `Action_PassBlock` | RT | `1` | `1` | 29 | START | 29 | 210 |
| ⚠️ START CHANGED | `Action_PassBlock` | RG | `11` | `11` | 29 | START | 31 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `13` | `13` | 29 | START | 29 | 38 |
| ✅ EXACT | `Action_PassBlock` | LT | `5` | `5` | 29 | START | 29 | 121 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `8` | `8` | 29 | START | 32 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | LB1 | `6` | `6` | 33 | START | 33 | 43 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `16` | `15` | 33 | END | 33 | 33 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `16` | `15` | 61 | START | 61 | 70 |
| ✅ EXACT | `Action_SecureCatch` | LB1 | `6` | `6` | 94 | START | 94 | 100 |
| ✅ EXACT | `Action_BallCarry` | LB1 | `6` | `6` | 101 | START | 101 | 210 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 87 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 210 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 121 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 38 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 86 | 88 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 93 | 210 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–35
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 35 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 88 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 126 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 125 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_RunOutRoute` | 33 | 43 | 11 | inferred_complete_timeline |
| `Action_RunOutRoute` | 45 | 93 | 49 | inferred_complete_timeline |
| `Action_SecureCatch` | 94 | 100 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 210 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 189 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 22–210 | 189 | 5 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 54–210 | 157 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 56–116 | 57 | 2 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 60–210 | 94 | 2 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 74–166 | 87 | 4 | Undefined position; Undefined team |
| `20` | `31` | Position_Unknown | Team_Unknown | 79–80 | 2 | 1 | Undefined position; Undefined team |
| `21` | `38` | Position_Unknown | Team_Unknown | 96–97 | 2 | 1 | Undefined position; Undefined team |
| `22` | `40` | Position_Unknown | Team_Unknown | 132–210 | 77 | 2 | Undefined position; Undefined team |
| `23` | `42` | Position_Unknown | Team_Unknown | 142–210 | 69 | 1 | Undefined position; Undefined team |
| `24` | `43` | Position_Unknown | Team_Unknown | 145–210 | 66 | 1 | Undefined position; Undefined team |
| `25` | `44` | Position_Unknown | Team_Unknown | 156–162 | 7 | 1 | Undefined position; Undefined team |
| `26` | `46` | Position_Unknown | Team_Unknown | 208–210 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `11` (RG): Annotated start 29 != Inferred start 31
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (3 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `8` (C): Annotated start 29 != Inferred start 32
- ⚠️ Ambiguous match for action `Action_RunOutRoute` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 44 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-189] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-121] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [33-43] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [45-93] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-35] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-88] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-38] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [86-88] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [93-210] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-104] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-210] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-107] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-131] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-97] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-184] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-162] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-210] for track '26' has 1 frames without a visible bounding box.
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