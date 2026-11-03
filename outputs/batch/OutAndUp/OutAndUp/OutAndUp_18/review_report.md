# Play-Annotation-Generator Annotation Review — OutAndUp_18

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_18`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 7
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `18` | `16` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `10` | `10` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_SellOut` | LB2 | defense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `11` | `11` |
| ✅ EXACT | `Action_RunGoRoute` | LB2 | defense | `5` | `5` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `1` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 38 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `18` | `16` | 36 | START | 41 | 51 |
| ✅ EXACT | `Action_PassBlock` | RT | `10` | `10` | 39 | START | 39 | 184 |
| ✅ EXACT | `Action_PassBlock` | LT | `4` | `4` | 39 | START | 39 | 167 |
| ✅ EXACT | `Action_PassBlock` | LG | `6` | `6` | 39 | START | 39 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `7` | `7` | 39 | START | 39 | 149 |
| ✅ EXACT | `Action_SellOut` | LB2 | `5` | `5` | 40 | START | 40 | 63 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `11` | `11` | 51 | END | 36 | 51 |
| ✅ EXACT | `Action_RunGoRoute` | LB2 | `5` | `5` | 64 | START | 64 | 295 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `11` | `11` | 142 | START | 142 | 151 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 105 | 70 | inferred_complete_timeline |
| `Action_None` | 109 | 141 | 33 | inferred_complete_timeline |
| `Action_None` | 145 | 165 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 143 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 167 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 175 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 149 | 111 | inferred_complete_timeline |
| `Action_PassBlock` | 151 | 216 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 184 | 146 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 61 | 26 | inferred_complete_timeline |
| `Action_None` | 64 | 67 | 4 | inferred_complete_timeline |
| `Action_None` | 84 | 89 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 35 | 20 | inferred_complete_timeline |
| `Action_None` | 36 | 40 | 5 | inferred_complete_timeline |
| `Action_None` | 47 | 60 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 175 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_SellOut` | 40 | 63 | 24 | inferred_complete_timeline |
| `Action_RunGoRoute` | 64 | 295 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 140 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 75 | 40 | inferred_complete_timeline |
| `Action_None` | 80 | 102 | 23 | inferred_complete_timeline |
| `Action_None` | 117 | 176 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 168 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 132 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–176 | 177 | 5 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–170 | 159 | 6 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 41–173 | 128 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 46–61 | 15 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 74–184 | 105 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 102–175 | 57 | 4 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 130–169 | 40 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 166–167 | 2 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 168–197 | 30 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 169–299 | 131 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 170–299 | 122 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 170–299 | 129 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 177–178 | 2 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 188–299 | 101 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 192–198 | 7 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 220–222 | 3 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 225–232 | 6 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 247–251 | 5 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 265–290 | 25 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `18` (Position_Unknown): Annotated start 36 != Inferred start 41
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 21: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Row 22: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [36-105] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-165] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-143] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-168] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-140] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-167] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [64-295] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-175] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [151-216] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-175] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-75] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-176] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-184] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-176] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-132] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-89] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-35] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-40] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-17] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-27] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-34] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-170] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-154] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-173] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-56] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-61] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-184] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-119] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-175] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-197] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-264] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-287] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-290] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-231] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-248] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-299] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-198] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-284] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-290] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.

</details>