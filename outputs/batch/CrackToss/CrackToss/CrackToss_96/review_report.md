# Play-Annotation-Generator Annotation Review — CrackToss_96

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_96`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | WR1 | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Toss` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `14` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `2` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 66 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `18` | `17` | 67 | START | 72 | 72 |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | `17` | `16` | 70 | START | 70 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | WR1 | `3` | `2` | 70 | START | 70 | 124 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 71 | END | 67 | 71 |
| ✅ EXACT | `Action_Toss` | QB | `12` | `11` | 75 | START | 75 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `4` | `3` | 100 | START | 100 | 168 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 166 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_SnapReceive` | 67 | 71 | 5 | inferred_complete_timeline |
| `Action_None` | 72 | 74 | 3 | inferred_complete_timeline |
| `Action_Toss` | 75 | 99 | 25 | inferred_complete_timeline |
| `Action_None` | 100 | 129 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 115 | 49 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_None` | 137 | 200 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 200 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PullBlock` | 70 | 124 | 55 | inferred_complete_timeline |
| `Action_PullBlock` | 132 | 148 | 17 | inferred_complete_timeline |
| `Action_None` | 173 | 178 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 109 | 43 | inferred_complete_timeline |
| `Action_None` | 111 | 200 | 90 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 110 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 200 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 81 | 15 | inferred_complete_timeline |
| `Action_None` | 88 | 96 | 9 | inferred_complete_timeline |
| `Action_None` | 100 | 103 | 4 | inferred_complete_timeline |
| `Action_None` | 105 | 117 | 13 | inferred_complete_timeline |
| `Action_None` | 119 | 200 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 200 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 127 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 132 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 175 | 109 | inferred_complete_timeline |
| `Action_None` | 182 | 187 | 6 | inferred_complete_timeline |
| `Action_None` | 191 | 194 | 4 | inferred_complete_timeline |
| `Action_None` | 198 | 200 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–200 | 148 | 4 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–192 | 192 | 3 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–200 | 201 | 2 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–200 | 196 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 61–200 | 140 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 72–112 | 41 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 95–172 | 78 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 105–200 | 92 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 109–110 | 2 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 119–200 | 82 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 124–200 | 74 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 158–200 | 43 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 158–200 | 43 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 181–200 | 20 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 182–187 | 6 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 190–200 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `18` (Position_Unknown): Annotated start 67 != Inferred start 72
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 194: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '2' (WR1) duration 97 frames exceeds threshold 90 frames [start=70, end=166].
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=72, end=71. Clamping end to start.
- ⚠️ Action 'Action_None' range [67-109] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-167] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [70-124] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [132-148] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-178] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [100-168] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [170-192] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-109] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-200] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-200] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-107] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-110] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-132] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-200] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [75-99] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-129] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-200] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-81] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-96] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-103] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-117] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-200] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-200] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [70-166] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-200] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-172] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-122] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-200] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-200] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-200] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-200] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-200] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.

</details>