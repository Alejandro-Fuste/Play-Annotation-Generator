# Play-Annotation-Generator Annotation Review — CrackToss_66

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_66`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 1
- **Action Segments:** 93
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | offense | `17` | `16` |
| ✅ EXACT | `Action_PullBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `17` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 28 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `18` | `17` | 29 | START | 29 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | `17` | `16` | 32 | START | 32 | 39 |
| ✅ EXACT | `Action_PullBlock` | RT | `5` | `4` | 32 | START | 32 | 93 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 41 | END | 29 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `7` | `6` | 42 | START | 42 | 78 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 95 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–102
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_SnapReceive` | 29 | 41 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 42 | 78 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 82 | 91 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 100 | 102 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 92 | 64 | inferred_complete_timeline |
| `Action_None` | 94 | 99 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 66 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_CrackBlock` | 32 | 39 | 8 | inferred_complete_timeline |
| `Action_CrackBlock` | 41 | 52 | 12 | inferred_complete_timeline |
| `Action_None` | 97 | 119 | 23 | inferred_complete_timeline |
| `Action_None` | 122 | 142 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 98 | 70 | inferred_complete_timeline |
| `Action_None` | 103 | 150 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 40 | 12 | inferred_complete_timeline |
| `Action_None` | 61 | 64 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PullBlock` | 32 | 93 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 150 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 113 | 85 | inferred_complete_timeline |
| `Action_None` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_None` | 127 | 150 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 55 | 27 | inferred_complete_timeline |
| `Action_None` | 57 | 60 | 4 | inferred_complete_timeline |
| `Action_None` | 64 | 121 | 58 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 106 | 78 | inferred_complete_timeline |
| `Action_None` | 131 | 149 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 109 | 81 | inferred_complete_timeline |
| `Action_None` | 113 | 149 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 113 | 85 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 150 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 101 | 73 | inferred_complete_timeline |
| `Action_None` | 114 | 150 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 52 | 24 | inferred_complete_timeline |
| `Action_None` | 54 | 62 | 9 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_None` | 74 | 144 | 71 | inferred_complete_timeline |
| `Action_None` | 147 | 148 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–150 | 138 | 7 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–63 | 63 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 5–10 | 6 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 11–150 | 119 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 31–142 | 20 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 37–38 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 48–96 | 49 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 70–111 | 35 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 72–146 | 66 | 8 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 84–150 | 57 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 93–94 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | 3 | 8 | 6 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 134: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ Row 134: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [29-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-92] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-99] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-106] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-109] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [32-93] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [42-78] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [82-91] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [95-96] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [100-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-101] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-40] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-64] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-55] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-60] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-66] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-113] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-52] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-62] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-144] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-144] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [32-39] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [41-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-119] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-10] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-12] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-36] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-150] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-36] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-91] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-99] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-111] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-91] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-98] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-109] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-120] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-129] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-106] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-123] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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