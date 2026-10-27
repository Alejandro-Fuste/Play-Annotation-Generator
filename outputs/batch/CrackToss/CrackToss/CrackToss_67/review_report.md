# Play-Annotation-Generator Annotation Review — CrackToss_67

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_67`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 2
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 4 | START | 4 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 4 | START | 4 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `16` | `Group` | 4 | START | 4 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 4 | START | 4 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 4 | START | 4 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 4 | START | 4 | 30 |
| ✅ EXACT | `Action_BallSnap` | RG | `6` | `5` | 31 | START | 31 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | `16` | `15` | 34 | START | 34 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | `5` | `4` | 34 | START | 34 | 73 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 40 | END | 31 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `10` | `9` | 41 | START | 41 | 99 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 100 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 4–106
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 30 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 40 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 41 | 99 | 59 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 106 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 4–150
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 30 | 27 | inferred_complete_timeline |
| `Action_None` | 31 | 81 | 51 | inferred_complete_timeline |
| `Action_None` | 83 | 103 | 21 | inferred_complete_timeline |
| `Action_None` | 110 | 113 | 4 | inferred_complete_timeline |
| `Action_None` | 115 | 150 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 4–108
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 33 | 30 | inferred_complete_timeline |
| `Action_CrackBlock` | 34 | 56 | 23 | inferred_complete_timeline |
| `Action_CrackBlock` | 65 | 76 | 12 | inferred_complete_timeline |
| `Action_CrackBlock` | 79 | 87 | 9 | inferred_complete_timeline |
| `Action_CrackBlock` | 89 | 100 | 12 | inferred_complete_timeline |
| `Action_None` | 101 | 108 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 4–150
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 30 | 27 | inferred_complete_timeline |
| `Action_None` | 31 | 141 | 111 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 4–150
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 30 | 27 | inferred_complete_timeline |
| `Action_BallSnap` | 31 | 40 | 10 | inferred_complete_timeline |
| `Action_None` | 41 | 62 | 22 | inferred_complete_timeline |
| `Action_None` | 67 | 150 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 4–102
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 33 | 30 | inferred_complete_timeline |
| `Action_PullBlock` | 34 | 73 | 40 | inferred_complete_timeline |
| `Action_PullBlock` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 81 | 100 | 20 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 4–149
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 30 | 27 | inferred_complete_timeline |
| `Action_None` | 31 | 141 | 111 | inferred_complete_timeline |
| `Action_None` | 146 | 149 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 4–100
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 30 | 27 | inferred_complete_timeline |
| `Action_None` | 31 | 31 | 1 | inferred_complete_timeline |
| `Action_None` | 61 | 64 | 4 | inferred_complete_timeline |
| `Action_None` | 77 | 86 | 10 | inferred_complete_timeline |
| `Action_None` | 89 | 96 | 8 | inferred_complete_timeline |
| `Action_None` | 98 | 100 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 64 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 2–3
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 3 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 4–150
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 30 | 27 | inferred_complete_timeline |
| `Action_None` | 31 | 101 | 71 | inferred_complete_timeline |
| `Action_None` | 106 | 108 | 3 | inferred_complete_timeline |
| `Action_None` | 122 | 150 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 4–43
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 30 | 27 | inferred_complete_timeline |
| `Action_None` | 31 | 43 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 4–56
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 30 | 27 | inferred_complete_timeline |
| `Action_None` | 31 | 56 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 4–53
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 30 | 27 | inferred_complete_timeline |
| `Action_None` | 31 | 53 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 91 | 61 | inferred_complete_timeline |
| `Action_None` | 102 | 122 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 2–3 | 2 | 1 | Undefined position; Undefined team |
| `10` | `11` | Position_Unknown | Team_Unknown | 4–125 | 86 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 4–150 | 138 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 6–149 | 131 | 6 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 27–33 | 7 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 57–142 | 50 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 58–105 | 45 | 4 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 67–91 | 25 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 84–108 | 22 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 86–147 | 57 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 91–144 | 53 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 102–150 | 49 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 128–150 | 23 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 136: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 136: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-91] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-122] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-64] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-3] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-3] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [34-73] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [75-76] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [81-100] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-62] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-81] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-103] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-150] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-101] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-53] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [41-99] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-66] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-76] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-86] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-141] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-56] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [34-56] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [65-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [79-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-30] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 31, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [31-31] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-64] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-86] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-96] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-114] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-30] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-34] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-128] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-33] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-142] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-64] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-94] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-105] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-91] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-106] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-147] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-144] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-150] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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