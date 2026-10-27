# Play-Annotation-Generator Annotation Review — CrackToss_39

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_39`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 67
- **Validation Warnings:** 74
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `10` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 65 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 66 | START | 66 | 75 |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | `18` | `17` | 69 | START | 69 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | `13` | `12` | 69 | START | 69 | 103 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 75 | END | 66 | 75 |
| ✅ EXACT | `Action_Toss` | QB | `7` | `6` | 79 | START | 79 | 95 |
| ✅ EXACT | `Action_BallCarry` | RB | `10` | `9` | 96 | START | 96 | 175 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_SnapReceive` | 66 | 75 | 10 | inferred_complete_timeline |
| `Action_None` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_Toss` | 79 | 95 | 17 | inferred_complete_timeline |
| `Action_None` | 96 | 128 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_BallCarry` | 96 | 175 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 175 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 97 | 32 | inferred_complete_timeline |
| `Action_None` | 102 | 175 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_BallSnap` | 66 | 75 | 10 | inferred_complete_timeline |
| `Action_None` | 76 | 175 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 112 | 47 | inferred_complete_timeline |
| `Action_None` | 118 | 161 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PullBlock` | 69 | 103 | 35 | inferred_complete_timeline |
| `Action_PullBlock` | 105 | 171 | 67 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 117 | 52 | inferred_complete_timeline |
| `Action_None` | 119 | 175 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 91 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 54 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 58 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_None` | 86 | 90 | 5 | inferred_complete_timeline |
| `Action_None` | 94 | 104 | 11 | inferred_complete_timeline |
| `Action_None` | 106 | 175 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 156 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 108 | 43 | inferred_complete_timeline |
| `Action_None` | 112 | 175 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 114 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 175 | 110 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–126 | 127 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–119 | 111 | 6 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 2–175 | 174 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 59–175 | 117 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 95–175 | 81 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 102–175 | 72 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 102–175 | 44 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 112–150 | 34 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 124–175 | 52 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 131–175 | 45 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 131–175 | 45 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 163–175 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 114 targets track ID '157', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 80: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '12' (RT) duration 103 frames exceeds threshold 90 frames [start=69, end=171].
- ⚠️ Action 'Action_None' range [66-126] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-112] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-108] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-175] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-91] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-128] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-117] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-156] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [96-175] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-114] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [69-103] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [105-171] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-97] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-175] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-32] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-54] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-104] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-175] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-72] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-107] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [69-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-175] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-147] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-175] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-175] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-139] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-175] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-175] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-175] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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