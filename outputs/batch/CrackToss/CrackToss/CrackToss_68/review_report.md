# Play-Annotation-Generator Annotation Review — CrackToss_68

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_68`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 106
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `21` | `20` |
| ✅ EXACT | `Action_CrackBlock` | WR2 | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR3 | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_PullBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_Toss` | QB | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `14` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 5 | START | 15 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 5 | START | 15 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `19` | `Group` | 5 | START | 15 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 5 | START | 15 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 5 | START | 15 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `23` | `Group` | 5 | START | 15 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 5 | START | 15 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 5 | START | 15 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 5 | START | 15 | 37 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `21` | `20` | 35 | START | 35 | 41 |
| ✅ EXACT | `Action_CrackBlock` | WR2 | `19` | `18` | 38 | START | 38 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR3 | `3` | `2` | 38 | START | 38 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `22` | `21` | 38 | START | 38 | 109 |
| ✅ EXACT | `Action_PullBlock` | RT | `9` | `8` | 38 | START | 38 | 175 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 41 | END | 35 | 41 |
| ✅ EXACT | `Action_Toss` | QB | `20` | `19` | 44 | START | 44 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `14` | `13` | 59 | START | 59 | 115 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 15–141
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_SnapReceive` | 35 | 41 | 7 | inferred_complete_timeline |
| `Action_None` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_Toss` | 44 | 58 | 15 | inferred_complete_timeline |
| `Action_None` | 59 | 109 | 51 | inferred_complete_timeline |
| `Action_None` | 114 | 141 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 15–143
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 58 | 44 | inferred_complete_timeline |
| `Action_BallCarry` | 59 | 115 | 57 | inferred_complete_timeline |
| `Action_BallCarry` | 121 | 124 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 128 | 135 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 137 | 143 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 15–149
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 37 | 23 | inferred_complete_timeline |
| `Action_CrackBlock` | 38 | 149 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 15–165
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 37 | 23 | inferred_complete_timeline |
| `Action_CrackBlock` | 38 | 108 | 71 | inferred_complete_timeline |
| `Action_CrackBlock` | 121 | 123 | 3 | inferred_complete_timeline |
| `Action_CrackBlock` | 128 | 165 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 15–175
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_None` | 35 | 117 | 83 | inferred_complete_timeline |
| `Action_None` | 121 | 134 | 14 | inferred_complete_timeline |
| `Action_None` | 136 | 175 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 15–175
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_None` | 35 | 175 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 15–145
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_None` | 35 | 115 | 81 | inferred_complete_timeline |
| `Action_None` | 119 | 145 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 15–167
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_None` | 35 | 109 | 75 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_None` | 120 | 140 | 21 | inferred_complete_timeline |
| `Action_None` | 146 | 150 | 5 | inferred_complete_timeline |
| `Action_None` | 152 | 167 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 15–175
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 37 | 23 | inferred_complete_timeline |
| `Action_PullBlock` | 38 | 175 | 138 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 15–175
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_None` | 35 | 117 | 83 | inferred_complete_timeline |
| `Action_None` | 121 | 130 | 10 | inferred_complete_timeline |
| `Action_None` | 133 | 162 | 30 | inferred_complete_timeline |
| `Action_None` | 168 | 175 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 15–98
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_None` | 35 | 49 | 15 | inferred_complete_timeline |
| `Action_None` | 52 | 98 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 15–56
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_None` | 35 | 56 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 15–106
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_None` | 35 | 99 | 65 | inferred_complete_timeline |
| `Action_None` | 103 | 106 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 15–175
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_None` | 35 | 107 | 73 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_None` | 119 | 175 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 15–146
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_None` | 35 | 115 | 81 | inferred_complete_timeline |
| `Action_None` | 117 | 146 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 15–175
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_None` | 35 | 123 | 89 | inferred_complete_timeline |
| `Action_None` | 128 | 135 | 8 | inferred_complete_timeline |
| `Action_None` | 138 | 144 | 7 | inferred_complete_timeline |
| `Action_None` | 149 | 175 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 15–175
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_None` | 35 | 150 | 116 | inferred_complete_timeline |
| `Action_None` | 154 | 175 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 15–118
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_None` | 35 | 118 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 13–14 | 2 | 1 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 15–74 | 50 | 3 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 15–95 | 81 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 15–155 | 141 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 15–175 | 152 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 55–170 | 103 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 80–88 | 4 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 91–93 | 3 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 92–175 | 72 | 5 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 94–115 | 21 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 125–140 | 16 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 128–175 | 48 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 129–175 | 47 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 155–170 | 16 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 168–175 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (4 segments found)

### Track Identity Issues

- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 92 targets track ID '111', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 72 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 137: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '8' (RT) duration 138 frames exceeds threshold 90 frames [start=38, end=175].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '21' (Unknown) duration 138 frames exceeds threshold 90 frames [start=38, end=175].
- ⚠️ Action 'Action_PreSnap' range [13-14] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-115] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-145] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [38-108] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [121-123] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [128-165] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-61] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-74] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-117] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-130] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-162] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-175] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-49] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-98] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-115] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-146] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [38-175] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-117] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-134] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-107] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-175] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-56] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-95] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [59-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [121-124] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [128-135] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [137-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-150] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-175] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-99] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-135] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-118] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [38-149] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-109] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-155] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [38-109] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [114-117] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [121-161] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [164-175] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-109] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-140] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-167] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-114] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-125] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-166] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-117] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-146] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-175] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-109] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-140] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-175] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-175] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-170] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-175] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.

</details>