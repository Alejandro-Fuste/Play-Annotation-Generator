# Play-Annotation-Generator Annotation Review — CrackToss_54

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_54`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 1
- **Action Segments:** 79
- **Validation Warnings:** 94
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_PullBlock` | TE2 | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | TE1 | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | TE1 | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `2` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `12` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 49 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 47 | START | 47 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | `17` | `16` | 50 | START | 50 | 76 |
| ✅ EXACT | `Action_PullBlock` | TE2 | `12` | `11` | 50 | START | 50 | 168 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | `6` | `5` | 50 | START | 50 | 150 |
| ✅ EXACT | `Action_SnapReceive` | TE1 | `11` | `10` | 51 | END | 47 | 51 |
| ✅ EXACT | `Action_Toss` | TE1 | `11` | `10` | 67 | START | 67 | 85 |
| ✅ EXACT | `Action_BallCarry` | RB | `2` | `1` | 86 | START | 86 | 137 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_BallCarry` | 86 | 137 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 51 | 5 | inferred_complete_timeline |
| `Action_None` | 52 | 66 | 15 | inferred_complete_timeline |
| `Action_Toss` | 67 | 85 | 19 | inferred_complete_timeline |
| `Action_None` | 86 | 108 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PullBlock` | 50 | 168 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PullBlock` | 50 | 150 | 101 | inferred_complete_timeline |
| `Action_PullBlock` | 153 | 154 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 120 | 74 | inferred_complete_timeline |
| `Action_None` | 125 | 165 | 41 | inferred_complete_timeline |
| `Action_None` | 170 | 175 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_BallSnap` | 47 | 51 | 5 | inferred_complete_timeline |
| `Action_None` | 52 | 175 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 175 | 129 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 68 | 22 | inferred_complete_timeline |
| `Action_None` | 75 | 81 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 46 | 8 | inferred_complete_timeline |
| `Action_None` | 47 | 115 | 69 | inferred_complete_timeline |
| `Action_None` | 125 | 155 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 86 | 40 | inferred_complete_timeline |
| `Action_None` | 91 | 98 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 91 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 152 | 106 | inferred_complete_timeline |
| `Action_None` | 155 | 175 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 85 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 175 | 129 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–175 | 172 | 5 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–175 | 96 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–175 | 175 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 34–93 | 59 | 3 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 63–93 | 13 | 3 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 70–130 | 40 | 7 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 71–175 | 88 | 3 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 88–132 | 45 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 95–175 | 79 | 2 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 106–110 | 5 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 109–175 | 67 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 124–175 | 52 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 132–175 | 42 | 3 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 148–175 | 28 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 166–167 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `20` | 6 | 47 | 25 | 59.5% | 7, 12, 14–27, 29 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 100 targets track ID '126', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 109: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 110: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '5' (LT) duration 105 frames exceeds threshold 90 frames [start=50, end=154].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '11' (TE2) duration 119 frames exceeds threshold 90 frames [start=50, end=168].
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-115] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-155] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [86-137] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-85] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-62] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-110] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [50-150] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [153-154] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-68] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-81] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-152] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-91] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-108] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [50-168] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-165] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-175] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-98] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [50-76] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [78-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 47, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [47-67] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-93] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-69] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-93] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-113] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-107] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-142] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-175] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-136] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-175] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-175] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-145] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-175] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.

</details>