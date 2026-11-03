# Play-Annotation-Generator Annotation Review — OutRoutes_147

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_147`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 65
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 43
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `14` | `14` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `18` | `18` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `18` | `18` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `12` | `12` | 20 | START | 59 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `13` | `13` | 20 | START | 20 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `14` | `14` | 20 | START | 20 | 21 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `1` | `1` | 27 | START | 27 | 106 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `18` | `18` | 27 | END | 27 | 27 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `18` | `18` | 75 | START | 75 | 82 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `1` | `1` | 107 | START | 107 | 116 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `1` | `1` | 117 | START | 117 | 148 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 139 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 150 | 8 | inferred_complete_timeline |

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
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_RunOutRoute` | 27 | 106 | 80 | inferred_complete_timeline |
| `Action_SecureCatch` | 107 | 116 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 117 | 148 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 62 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 79 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 85 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 107 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 68 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 85 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 121 | 99 | inferred_complete_timeline |
| `Action_PassBlock` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 142 | 148 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 87 | 68 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 139 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 148 | 150 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 48 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 150 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 150 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 150 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

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
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 130 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
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
| `18` | `18` | Position_Unknown | Team_Unknown | 13–150 | 136 | 6 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 29–140 | 108 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 56–139 | 81 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 72–129 | 43 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 118–150 | 30 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 120–133 | 14 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 122–133 | 9 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 137–138 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 147–150 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 57 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [117-148] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-118] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-139] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-130] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-62] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-79] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-85] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-107] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-145] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-85] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-139] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [148-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-21] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-121] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [130-132] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [142-148] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-150] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-26] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-138] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-150] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-53] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-140] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-57] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-61] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-139] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-99] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-112] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-124] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-129] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-134] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-124] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-133] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-138] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-150] for track '26' has 1 frames without a visible bounding box.
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