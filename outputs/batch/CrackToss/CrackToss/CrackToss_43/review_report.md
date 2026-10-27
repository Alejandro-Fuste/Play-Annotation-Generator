# Play-Annotation-Generator Annotation Review — CrackToss_43

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_43`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 90
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | TE2 | offense | `8` | `7` |
| ✅ EXACT | `Action_PullBlock` | TE1 | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Toss` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `14` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `14` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 70 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `17` | `16` | 68 | START | 68 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | TE2 | `8` | `7` | 71 | START | 71 | 120 |
| ✅ EXACT | `Action_PullBlock` | TE1 | `4` | `3` | 71 | START | 71 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | `6` | `5` | 71 | START | 71 | 175 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 79 | END | 68 | 79 |
| ✅ EXACT | `Action_Toss` | QB | `12` | `11` | 83 | START | 83 | 91 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `14` | `13` | 92 | START | 92 | 163 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_SnapReceive` | 68 | 79 | 12 | inferred_complete_timeline |
| `Action_None` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_Toss` | 83 | 91 | 9 | inferred_complete_timeline |
| `Action_None` | 92 | 137 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 117 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_BallCarry` | 92 | 163 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PullBlock` | 71 | 200 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_CrackBlock` | 71 | 120 | 50 | inferred_complete_timeline |
| `Action_CrackBlock` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_CrackBlock` | 128 | 200 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 81 | 14 | inferred_complete_timeline |
| `Action_None` | 83 | 123 | 41 | inferred_complete_timeline |
| `Action_None` | 129 | 200 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 200 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PullBlock` | 71 | 175 | 105 | inferred_complete_timeline |
| `Action_PullBlock` | 177 | 181 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 189 | 192 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 161 | 94 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 158 | 91 | inferred_complete_timeline |
| `Action_None` | 161 | 200 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_BallSnap` | 68 | 79 | 12 | inferred_complete_timeline |
| `Action_None` | 80 | 200 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 131 | 64 | inferred_complete_timeline |
| `Action_None` | 133 | 200 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 169 | 102 | inferred_complete_timeline |
| `Action_None` | 181 | 200 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 150 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 200 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 200 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 68 | 193 | 126 | inferred_complete_timeline |
| `Action_None` | 195 | 200 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–200 | 200 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–163 | 160 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–200 | 201 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 82–85 | 4 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 100–133 | 21 | 3 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 104–106 | 3 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 127–200 | 73 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 134–149 | 12 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 159–200 | 26 | 4 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 168–200 | 33 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 170–200 | 26 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 170–200 | 31 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 187–198 | 12 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 187–200 | 14 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 197–200 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 126 targets track ID '152', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 88: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ Row 88: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ Row 88: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '3' (TE1) duration 130 frames exceeds threshold 90 frames [start=71, end=200].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '5' (RT) duration 122 frames exceeds threshold 90 frames [start=71, end=192].
- ⚠️ Action 'Action_None' range [68-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-169] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-200] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-158] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-200] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [71-200] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-200] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [71-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [177-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [189-192] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-193] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [71-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [122-123] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [128-200] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-161] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-131] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-200] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-130] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-200] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-137] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [92-163] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-200] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-200] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-200] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-200] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-81] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-200] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-85] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-117] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-133] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-191] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-143] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-167] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-200] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-188] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-198] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-200] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>