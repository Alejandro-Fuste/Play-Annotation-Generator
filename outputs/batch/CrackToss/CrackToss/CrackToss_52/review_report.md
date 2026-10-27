# Play-Annotation-Generator Annotation Review — CrackToss_52

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_52`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 88
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | TE | offense | `8` | `7` |
| ✅ EXACT | `Action_PullBlock` | RT | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Toss` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 50 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 51 | START | 51 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | TE | `8` | `7` | 54 | START | 54 | 133 |
| ✅ EXACT | `Action_PullBlock` | RT | `2` | `1` | 54 | START | 54 | 163 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 63 | END | 51 | 63 |
| ✅ EXACT | `Action_Toss` | QB | `15` | `14` | 67 | START | 67 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `5` | 86 | START | 86 | 138 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_SnapReceive` | 51 | 63 | 13 | inferred_complete_timeline |
| `Action_None` | 64 | 66 | 3 | inferred_complete_timeline |
| `Action_Toss` | 67 | 85 | 19 | inferred_complete_timeline |
| `Action_None` | 86 | 122 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_BallCarry` | 86 | 138 | 53 | inferred_complete_timeline |
| `Action_BallCarry` | 140 | 143 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_CrackBlock` | 54 | 133 | 80 | inferred_complete_timeline |
| `Action_CrackBlock` | 143 | 146 | 4 | inferred_complete_timeline |
| `Action_CrackBlock` | 151 | 152 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 132 | 82 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 175 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 74 | 24 | inferred_complete_timeline |
| `Action_None` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_None` | 95 | 105 | 11 | inferred_complete_timeline |
| `Action_None` | 108 | 137 | 30 | inferred_complete_timeline |
| `Action_None` | 164 | 175 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_BallSnap` | 51 | 63 | 13 | inferred_complete_timeline |
| `Action_None` | 64 | 97 | 34 | inferred_complete_timeline |
| `Action_None` | 101 | 171 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 155 | 105 | inferred_complete_timeline |
| `Action_None` | 157 | 172 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PullBlock` | 54 | 163 | 110 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 175 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 113 | 63 | inferred_complete_timeline |
| `Action_None` | 120 | 126 | 7 | inferred_complete_timeline |
| `Action_None` | 172 | 175 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 24 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 34 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 50 | 1 | inferred_complete_timeline |
| `Action_None` | 51 | 62 | 12 | inferred_complete_timeline |
| `Action_None` | 73 | 77 | 5 | inferred_complete_timeline |
| `Action_None` | 79 | 175 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 66 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 128 | 78 | inferred_complete_timeline |
| `Action_None` | 134 | 139 | 6 | inferred_complete_timeline |
| `Action_None` | 143 | 163 | 21 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 103 | 53 | inferred_complete_timeline |
| `Action_None` | 119 | 122 | 4 | inferred_complete_timeline |
| `Action_None` | 128 | 175 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 86 | 175 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 175 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–40
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 40 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 66–71 | 6 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 73–175 | 85 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 75–148 | 72 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 80–175 | 89 | 4 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 83–91 | 4 | 2 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 99–128 | 30 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 104–175 | 68 | 3 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 111–175 | 65 | 1 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 133–175 | 43 | 1 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 133–175 | 43 | 1 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 156–157 | 2 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 161–172 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 111 targets track ID '133', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '1' (RT) duration 110 frames exceeds threshold 90 frames [start=54, end=163].
- ⚠️ Action 'Action_None' range [51-175] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [54-163] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-175] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-132] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [86-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [140-143] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-113] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-126] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [54-133] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [143-146] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [151-152] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-155] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-172] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-128] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-139] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-163] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-105] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-137] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-103] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-97] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-171] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-175] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-24] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-34] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-62] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-175] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-71] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-175] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-91] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-148] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-140] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-157] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-143] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-175] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-175] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-175] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-172] for track '28' has 1 frames without a visible bounding box.
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

</details>