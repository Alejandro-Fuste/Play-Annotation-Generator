# Play-Annotation-Generator Annotation Review — Draw_91

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_91`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 31 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `8` | 32 | START | 32 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `2` | `1` | 35 | START | 35 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `3` | `2` | 35 | START | 35 | 122 |
| ✅ EXACT | `Action_PassBlock` | LG | `4` | `3` | 35 | START | 35 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `8` | `7` | 35 | START | 35 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `9` | `8` | 35 | START | 48 | 98 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 47 | END | 32 | 47 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `7` | `6` | 50 | START | 50 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `7` | `6` | 74 | START | 74 | 133 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 122 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 31 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 32 | 47 | 16 | inferred_complete_timeline |
| `Action_None` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 50 | 73 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 74 | 133 | 60 | inferred_complete_timeline |
| `Action_BallCarry` | 136 | 269 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 59 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 122 | 88 | inferred_complete_timeline |
| `Action_None` | 123 | 269 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 120 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 47 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 98 | 51 | inferred_complete_timeline |
| `Action_PassBlock` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 104 | 113 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 117 | 3 | inferred_complete_timeline |
| `Action_None` | 124 | 269 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 112 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 122 | 88 | inferred_complete_timeline |
| `Action_None` | 123 | 165 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 31 | 10 | inferred_complete_timeline |
| `Action_None` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_None` | 91 | 107 | 17 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 56 | 25 | inferred_complete_timeline |
| `Action_None` | 79 | 80 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 75 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `11` | Position_Unknown | Team_Unknown | 12–248 | 227 | 5 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 24–30 | 7 | 1 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 41–269 | 227 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 53–269 | 210 | 4 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 64–147 | 84 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 65–139 | 68 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 111–135 | 23 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 111–114 | 4 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 129–190 | 62 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 132–264 | 130 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 140–269 | 130 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 145–269 | 125 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 145–152 | 8 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 167–269 | 103 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 173–269 | 95 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 194–269 | 76 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 216–269 | 41 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 257–269 | 13 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 261–269 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [32–47], lower_priority='Action_PassBlock' annotated_start=35, effective_Action_PassBlock_start=48.
- ⚠️ Action 'Action_None' range [32-59] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-112] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-56] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-75] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [74-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-165] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [48-98] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [101-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [104-113] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [115-117] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-33] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-58] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-245] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-30] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-269] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-67] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-147] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-139] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-131] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-190] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-165] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-264] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-152] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-222] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.

</details>