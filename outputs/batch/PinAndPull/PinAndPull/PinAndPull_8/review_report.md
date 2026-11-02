# Play-Annotation-Generator Annotation Review — PinAndPull_8

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PinAndPull_8`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_PinAndPull`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 66
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RB | offense | `17` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 64 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 65 | START | 65 | 80 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `14` | `13` | 67 | START | 81 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `18` | `17` | 67 | START | 67 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RB | `17` | `16` | 67 | START | 67 | 122 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 80 | END | 65 | 80 |
| ✅ EXACT | `Action_BallCarry` | QB | `15` | `14` | 91 | START | 91 | 155 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 159 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_SnapReceive` | 65 | 80 | 16 | inferred_complete_timeline |
| `Action_None` | 81 | 90 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 91 | 155 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 67 | 122 | 56 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 131 | 139 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 122 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 112 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 102 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PullBlock` | 67 | 113 | 47 | inferred_complete_timeline |
| `Action_PullBlock` | 120 | 159 | 40 | inferred_complete_timeline |
| `Action_None` | 160 | 180 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_BallSnap` | 65 | 80 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 81 | 159 | 79 | inferred_complete_timeline |
| `Action_None` | 160 | 179 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 180 | 116 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 126 | 62 | inferred_complete_timeline |
| `Action_None` | 129 | 175 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 180 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 76 | 12 | inferred_complete_timeline |
| `Action_None` | 147 | 155 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 180 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 180 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 145 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 121 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 98 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 101 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 179 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 148 | 84 | inferred_complete_timeline |
| `Action_None` | 157 | 160 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 77–172 | 87 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 88–180 | 92 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 101–180 | 72 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 107–163 | 56 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 150–180 | 30 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 156–180 | 23 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 162–165 | 4 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 167–180 | 14 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 172–173 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `14` (C): Annotated start 67 != Inferred start 81
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 18: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (C) duration 93 frames exceeds threshold 90 frames [start=67, end=159].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [65–80], lower_priority='Action_DownBlock' annotated_start=67, effective_Action_DownBlock_start=81.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '17' (LG) duration 93 frames exceeds threshold 90 frames [start=67, end=159].
- ⚠️ Action 'Action_None' range [65-112] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-101] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-102] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-121] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-179] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-148] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-180] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-126] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-175] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-179] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [91-155] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [67-122] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [131-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [67-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [120-159] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-172] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-163] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-139] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-180] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-163] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-169] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-175] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-180] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '27' has 1 frames without a visible bounding box.
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