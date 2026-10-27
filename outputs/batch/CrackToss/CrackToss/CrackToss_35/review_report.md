# Play-Annotation-Generator Annotation Review — CrackToss_35

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_35`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `13` | `12` |
| ⚠️ START CHANGED | `Action_PullBlock` | Position_Unknown | Team_Unknown | `22` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Toss` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 21 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 22 | START | 22 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | `13` | `12` | 25 | START | 25 | 29 |
| ⚠️ START CHANGED | `Action_PullBlock` | Position_Unknown | `22` | `17` | 25 | START | 43 | 83 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 30 | END | 22 | 30 |
| ✅ EXACT | `Action_Toss` | QB | `6` | `5` | 32 | START | 32 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `2` | 50 | START | 50 | 99 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 83 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 30 | 9 | inferred_complete_timeline |
| `Action_None` | 31 | 31 | 1 | inferred_complete_timeline |
| `Action_Toss` | 32 | 49 | 18 | inferred_complete_timeline |
| `Action_None` | 50 | 125 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_BallCarry` | 50 | 99 | 50 | inferred_complete_timeline |
| `Action_BallCarry` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 112 | 113 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 125 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 99 | 78 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 121 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 125 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–30
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_BallSnap` | 22 | 30 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 79 | 58 | inferred_complete_timeline |
| `Action_None` | 81 | 125 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 39 | 18 | inferred_complete_timeline |
| `Action_None` | 43 | 56 | 14 | inferred_complete_timeline |
| `Action_None` | 59 | 99 | 41 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 21 | 3 | inferred_complete_timeline |
| `Action_None` | 22 | 29 | 8 | inferred_complete_timeline |
| `Action_None` | 40 | 100 | 61 | inferred_complete_timeline |
| `Action_None` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_None` | 108 | 110 | 3 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 113 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 82 | 61 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 15–120 | 106 | 2 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 17–103 | 71 | 8 | Undefined position; Undefined team |
| `13` | `16` | Position_Unknown | Team_Unknown | 41–125 | 85 | 1 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 41–124 | 74 | 4 | Undefined position; Undefined team |
| `15` | `20` | Position_Unknown | Team_Unknown | 43–125 | 82 | 2 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 43–99 | 57 | 1 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 43–99 | 57 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 44–95 | 47 | 2 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 44–125 | 82 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 45–125 | 70 | 3 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 47–103 | 52 | 4 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 54–70 | 17 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 77–119 | 40 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 124–125 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `13` (5 segments found)
- ⚠️ `Action_PullBlock` for actor_track_id `22` (Position_Unknown): Annotated start 25 != Inferred start 43
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 55 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [22-125] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-113] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [50-99] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [102-103] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [112-113] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-82] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-99] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-125] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-125] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-79] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-125] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-39] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-56] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-99] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-29] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-100] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [22-30] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-120] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [25-29] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [40-41] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [43-67] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [70-71] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [74-83] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-67] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-107] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-99] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-99] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-99] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-68] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-95] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-67] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-105] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-67] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-99] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-70] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-114] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>