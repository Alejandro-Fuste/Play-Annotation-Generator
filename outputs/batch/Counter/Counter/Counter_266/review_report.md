# Play-Annotation-Generator Annotation Review — Counter_266

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_266`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 64
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_PullBlock` | DT2 | defense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RB2 | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `3` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `8` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 35 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 33 | START | 33 | 45 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `10` | `9` | 36 | START | 46 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `9` | `8` | 36 | START | 36 | 124 |
| ✅ EXACT | `Action_PullBlock` | DT2 | `15` | `14` | 36 | START | 36 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RB2 | `3` | `2` | 36 | START | 36 | 84 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 45 | END | 33 | 45 |
| ✅ EXACT | `Action_BallCarry` | QB | `4` | `3` | 74 | START | 74 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 127 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 33 | 45 | 13 | inferred_complete_timeline |
| `Action_None` | 46 | 73 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 74 | 210 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 65 | 33 | inferred_complete_timeline |
| `Action_None` | 72 | 210 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 36 | 84 | 49 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 86 | 91 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 178 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 210 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_BallSnap` | 33 | 45 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 46 | 127 | 82 | inferred_complete_timeline |
| `Action_None` | 128 | 141 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_DownBlock` | 36 | 124 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 81 | 49 | inferred_complete_timeline |
| `Action_None` | 101 | 105 | 5 | inferred_complete_timeline |
| `Action_None` | 122 | 125 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 87 | 55 | inferred_complete_timeline |
| `Action_None` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_None` | 93 | 126 | 34 | inferred_complete_timeline |
| `Action_None` | 128 | 210 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 107 | 75 | inferred_complete_timeline |
| `Action_None` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_None` | 134 | 138 | 5 | inferred_complete_timeline |
| `Action_None` | 152 | 210 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 65 | 33 | inferred_complete_timeline |
| `Action_None` | 67 | 71 | 5 | inferred_complete_timeline |
| `Action_None` | 73 | 136 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PullBlock` | 36 | 127 | 92 | inferred_complete_timeline |
| `Action_None` | 128 | 179 | 52 | inferred_complete_timeline |
| `Action_None` | 182 | 186 | 5 | inferred_complete_timeline |
| `Action_None` | 190 | 195 | 6 | inferred_complete_timeline |
| `Action_None` | 206 | 210 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 118 | 86 | inferred_complete_timeline |
| `Action_None` | 148 | 210 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 171 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 210 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 210 | 178 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `20` | Position_Unknown | Team_Unknown | 82–210 | 129 | 1 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 102–210 | 109 | 1 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 103–210 | 108 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 112–210 | 86 | 2 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 128–196 | 66 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 130–210 | 81 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 134–210 | 77 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 165–166 | 2 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 195–200 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `10` (C): Annotated start 36 != Inferred start 46
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '9' (C) duration 92 frames exceeds threshold 90 frames [start=36, end=127].
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [33–45], lower_priority='Action_DownBlock' annotated_start=36, effective_Action_DownBlock_start=46.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '14' (DT2) duration 92 frames exceeds threshold 90 frames [start=36, end=127].
- ⚠️ Action 'Action_None' range [33-81] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-105] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-125] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-87] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-126] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [36-84] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [86-91] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [74-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-171] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-178] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-65] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [36-124] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [46-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-141] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-118] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-107] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-138] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-71] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-179] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-195] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-210] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-119] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-210] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '24' has 2 frames without a visible bounding box.
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