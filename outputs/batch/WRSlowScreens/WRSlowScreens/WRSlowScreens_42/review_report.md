# Play-Annotation-Generator Annotation Review — WRSlowScreens_42

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `WRSlowScreens_42`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_WRSlowScreens`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 71
- **Validation Warnings:** 91
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
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReleaseToScreen` | LG | offense | `10` | `10` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | Position_Unknown | Team_Unknown | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 13 | START | 13 | 31 |
| ✅ EXACT | `Action_PassBlock` | LG | `10` | `10` | 16 | START | 16 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `11` | `11` | 16 | START | 32 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `2` | `2` | 16 | START | 16 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `5` | `5` | 16 | START | 16 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `6` | `6` | 16 | START | 16 | 150 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 31 | END | 13 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReleaseToScreen` | LG | `10` | `10` | 44 | START | 44 | 50 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `7` | `7` | 77 | START | 77 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | Position_Unknown | `16` | `16` | 106 | START | 107 | 155 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_SnapReceive` | 13 | 31 | 19 | inferred_complete_timeline |
| `Action_None` | 32 | 76 | 45 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 77 | 87 | 11 | inferred_complete_timeline |
| `Action_None` | 88 | 100 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 35 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 90 | 75 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 103 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 43 | 28 | inferred_complete_timeline |
| `Action_ReleaseToScreen` | 44 | 50 | 7 | inferred_complete_timeline |
| `Action_ReleaseToScreen` | 55 | 180 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 13 | 31 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 70 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 180 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 150 | 135 | inferred_complete_timeline |
| `Action_PassBlock` | 156 | 180 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 99 | 84 | inferred_complete_timeline |
| `Action_PassBlock` | 127 | 180 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 132 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 41 | 29 | inferred_complete_timeline |
| `Action_None` | 43 | 47 | 5 | inferred_complete_timeline |
| `Action_None` | 51 | 92 | 42 | inferred_complete_timeline |
| `Action_None` | 104 | 116 | 13 | inferred_complete_timeline |
| `Action_None` | 125 | 180 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 17 | 24 | 8 | inferred_complete_timeline |
| `Action_None` | 31 | 36 | 6 | inferred_complete_timeline |
| `Action_None` | 44 | 112 | 69 | inferred_complete_timeline |
| `Action_None` | 114 | 180 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 121 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 91 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 53 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 21–180 | 119 | 4 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 31–39 | 9 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 46–180 | 132 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 91–180 | 88 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 91–180 | 90 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 98–180 | 79 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 98–180 | 82 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 100–137 | 38 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 123–180 | 58 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 129–166 | 36 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 132–155 | 24 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 137–180 | 43 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 137–180 | 44 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 137–180 | 44 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 141–180 | 40 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 149–180 | 32 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 156–180 | 24 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ReleaseToScreen` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunAfterCatch` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [13–31], lower_priority='Action_PassBlock' annotated_start=16, effective_Action_PassBlock_start=32.
- ⚠️ Action 'Action_None' range [13-53] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-35] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-90] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-103] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-121] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-99] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [127-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [156-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-100] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-132] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-41] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-47] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-92] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-116] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReleaseToScreen' range [44-50] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReleaseToScreen' range [55-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-70] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-180] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-24] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-36] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-112] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-26] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-33] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-173] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-39] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-119] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [107-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [157-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-171] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-137] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-161] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-155] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-165] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-180] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-180] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-180] for track '29' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

</details>