# Play-Annotation-Generator Annotation Review — CrackToss_15

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_15`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RB | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | offense | `6` | `5` |
| ✅ EXACT | `Action_CrackBlock` | WR3 | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 0 | START | 0 | 19 |
| ✅ EXACT | `Action_BallSnap` | RB | `2` | `1` | 17 | START | 17 | 19 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `18` | `17` | 19 | END | 18 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | `6` | `5` | 20 | START | 20 | 41 |
| ✅ EXACT | `Action_CrackBlock` | WR3 | `8` | `7` | 20 | START | 20 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | `15` | `14` | 20 | START | 20 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | Position_Unknown | `18` | `17` | 24 | START | 24 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `2` | `1` | 51 | START | 51 | 108 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 119 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–131
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_BallSnap` | 17 | 19 | 3 | inferred_complete_timeline |
| `Action_None` | 20 | 50 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 51 | 108 | 58 | inferred_complete_timeline |
| `Action_BallCarry` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 78 | 62 | inferred_complete_timeline |
| `Action_None` | 111 | 115 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_CrackBlock` | 20 | 41 | 22 | inferred_complete_timeline |
| `Action_CrackBlock` | 47 | 49 | 3 | inferred_complete_timeline |
| `Action_CrackBlock` | 54 | 60 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_CrackBlock` | 20 | 37 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 150 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PullBlock` | 20 | 93 | 74 | inferred_complete_timeline |
| `Action_PullBlock` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_None` | 127 | 133 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–27
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 27 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 29 | 13 | inferred_complete_timeline |
| `Action_None` | 94 | 96 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 56 | 40 | inferred_complete_timeline |
| `Action_None` | 65 | 69 | 5 | inferred_complete_timeline |
| `Action_None` | 71 | 85 | 15 | inferred_complete_timeline |
| `Action_None` | 96 | 120 | 25 | inferred_complete_timeline |
| `Action_None` | 122 | 130 | 9 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–22
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 22 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 66 | 50 | inferred_complete_timeline |
| `Action_None` | 68 | 69 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 81 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 91 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 90 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 150 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 136 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 150 | 134 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 13–148 | 129 | 7 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 55–105 | 28 | 6 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 74–117 | 37 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 80–114 | 24 | 4 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 87–150 | 25 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 91–144 | 54 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 93–96 | 4 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 129–150 | 17 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 134–150 | 17 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 136–150 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Toss` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '14' (LT) duration 100 frames exceeds threshold 90 frames [start=20, end=119].
- ⚠️ Action 'Action_None' range [17-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [51-108] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [130-131] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-78] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-66] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [20-41] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [47-49] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [54-60] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-91] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [20-37] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-90] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-56] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-69] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-85] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-130] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 17, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [17-22] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [20-93] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [104-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [113-114] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-133] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-29] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-27] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-15] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [24-28] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [30-37] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-148] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-64] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-75] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-80] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-96] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-117] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-94] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-135] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-150] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-144] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-150] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-150] for track '26' has 1 frames without a visible bounding box.
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