# Play-Annotation-Generator Annotation Review — CrackToss_36

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_36`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | LB1 | defense | `5` | `4` |
| ✅ EXACT | `Action_PullBlock` | RT | offense | `10` | `9` |
| ✅ EXACT | `Action_PullBlock` | TE3 | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Toss` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `2` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 43 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 15 | START | 15 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | LB1 | `5` | `4` | 18 | START | 18 | 57 |
| ✅ EXACT | `Action_PullBlock` | RT | `10` | `9` | 18 | START | 18 | 91 |
| ✅ EXACT | `Action_PullBlock` | TE3 | `2` | `1` | 18 | START | 18 | 91 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 22 | END | 15 | 22 |
| ✅ EXACT | `Action_Toss` | QB | `13` | `12` | 24 | START | 24 | 43 |
| ✅ EXACT | `Action_BallCarry` | RB | `8` | `7` | 44 | START | 44 | 125 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 91 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_SnapReceive` | 15 | 22 | 8 | inferred_complete_timeline |
| `Action_None` | 23 | 23 | 1 | inferred_complete_timeline |
| `Action_Toss` | 24 | 43 | 20 | inferred_complete_timeline |
| `Action_None` | 44 | 75 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_BallCarry` | 44 | 125 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 89 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 18 | 91 | 74 | inferred_complete_timeline |
| `Action_None` | 92 | 125 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_None` | 51 | 125 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_BallSnap` | 15 | 22 | 8 | inferred_complete_timeline |
| `Action_None` | 23 | 125 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 118 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 18 | 91 | 74 | inferred_complete_timeline |
| `Action_None` | 92 | 108 | 17 | inferred_complete_timeline |
| `Action_None` | 114 | 125 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 43 | 29 | inferred_complete_timeline |
| `Action_None` | 45 | 47 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 30 | 16 | inferred_complete_timeline |
| `Action_None` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_None` | 43 | 86 | 44 | inferred_complete_timeline |
| `Action_None` | 98 | 125 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 24 | 10 | inferred_complete_timeline |
| `Action_None` | 33 | 60 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 23 | 125 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_CrackBlock` | 18 | 57 | 40 | inferred_complete_timeline |
| `Action_CrackBlock` | 59 | 71 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 41 | 27 | inferred_complete_timeline |
| `Action_None` | 43 | 58 | 16 | inferred_complete_timeline |
| `Action_None` | 60 | 73 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 18 | 4 | inferred_complete_timeline |
| `Action_None` | 21 | 73 | 53 | inferred_complete_timeline |
| `Action_None` | 80 | 125 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 76 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 63 | 49 | inferred_complete_timeline |
| `Action_None` | 68 | 78 | 11 | inferred_complete_timeline |
| `Action_None` | 80 | 125 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–125 | 126 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 37–120 | 77 | 3 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 43–125 | 82 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 44–45 | 2 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 44–91 | 21 | 4 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 51–68 | 7 | 2 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 64–78 | 14 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 66–67 | 2 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 74–103 | 29 | 2 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 74–119 | 46 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 98–107 | 10 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 104–125 | 22 | 1 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 107–125 | 19 | 1 | Undefined position; Undefined team |
| `30` | `48` | Position_Unknown | Team_Unknown | 118–125 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 74: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [15-89] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-125] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-118] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-34] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-125] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [18-57] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [59-71] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-125] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-76] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [44-125] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-41] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-58] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-73] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-108] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-43] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-30] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-33] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-86] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-125] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-125] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-24] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-125] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-18] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-125] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-63] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-78] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-74] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-107] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-53] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-81] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-68] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-69] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-78] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-96] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-103] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-119] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-107] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-125] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-125] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-125] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.

</details>