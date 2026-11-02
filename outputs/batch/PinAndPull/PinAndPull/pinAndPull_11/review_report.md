# Play-Annotation-Generator Annotation Review — pinAndPull_11

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `pinAndPull_11`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_PinAndPull`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `2` | `1` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_PullLeadBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 31 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 32 | START | 32 | 43 |
| ✅ EXACT | `Action_DownBlock` | RT | `2` | `1` | 35 | START | 35 | 129 |
| ✅ EXACT | `Action_PullBlock` | RG | `5` | `4` | 35 | START | 35 | 129 |
| ✅ EXACT | `Action_PullLeadBlock` | LG | `6` | `5` | 35 | START | 35 | 64 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 43 | END | 32 | 43 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `6` | 47 | START | 47 | 67 |
| ✅ EXACT | `Action_BallCarry` | RB | `4` | `3` | 68 | START | 68 | 168 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 129 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_SnapReceive` | 32 | 43 | 12 | inferred_complete_timeline |
| `Action_None` | 44 | 46 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 47 | 67 | 21 | inferred_complete_timeline |
| `Action_None` | 68 | 98 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_BallCarry` | 68 | 168 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 155 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 35 | 64 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 43 | 12 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PullBlock` | 35 | 129 | 95 | inferred_complete_timeline |
| `Action_None` | 130 | 210 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_DownBlock` | 35 | 129 | 95 | inferred_complete_timeline |
| `Action_None` | 130 | 210 | 81 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 210 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 119 | 88 | inferred_complete_timeline |
| `Action_None` | 123 | 210 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 130 | 99 | inferred_complete_timeline |
| `Action_None` | 132 | 210 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 38 | 7 | inferred_complete_timeline |
| `Action_None` | 41 | 43 | 3 | inferred_complete_timeline |
| `Action_None` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_None` | 50 | 55 | 6 | inferred_complete_timeline |
| `Action_None` | 59 | 93 | 35 | inferred_complete_timeline |
| `Action_None` | 96 | 102 | 7 | inferred_complete_timeline |
| `Action_None` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_None` | 112 | 210 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 43 | 12 | inferred_complete_timeline |
| `Action_None` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_None` | 50 | 92 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 210 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 31 | 19 | inferred_complete_timeline |
| `Action_None` | 32 | 52 | 21 | inferred_complete_timeline |
| `Action_None` | 88 | 169 | 82 | inferred_complete_timeline |
| `Action_None` | 172 | 210 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–148 | 149 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 37–152 | 91 | 2 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 80–210 | 131 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 84–125 | 42 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 84–210 | 112 | 6 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 104–210 | 89 | 3 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 105–210 | 101 | 3 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 128–175 | 27 | 4 | Undefined position; Undefined team |
| `22` | `33` | Position_Unknown | Team_Unknown | 165–210 | 46 | 1 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 168–210 | 35 | 4 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 181–210 | 13 | 2 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 206–209 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 24: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '1' (RT) duration 95 frames exceeds threshold 90 frames [start=35, end=129].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '4' (RG) duration 95 frames exceeds threshold 90 frames [start=35, end=129].
- ⚠️ Action 'Action_None' range [32-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [35-129] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-130] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [68-168] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [35-64] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-148] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-155] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-119] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-38] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-43] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-48] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-102] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-43] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-48] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-92] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-52] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-169] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-152] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-162] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-170] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-194] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-147] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-174] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-201] for track '20' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-151] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-174] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-181] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-191] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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

</details>