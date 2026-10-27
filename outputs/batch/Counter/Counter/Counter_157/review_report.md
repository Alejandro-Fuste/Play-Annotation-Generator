# Play-Annotation-Generator Annotation Review — Counter_157

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_157`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_DownBlock` | LB1 | defense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | DE2 | defense | `4` | `3` |
| ✅ EXACT | `Action_PlaySideFakeStep` | TE | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | DT2 | defense | `6` | `5` |
| ✅ EXACT | `Action_Handoff` | DT2 | defense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | TE | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `14` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 55 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `19` | `18` | 56 | START | 56 | 59 |
| ✅ EXACT | `Action_DownBlock` | LB1 | `10` | `9` | 60 | START | 60 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `19` | `18` | 60 | START | 60 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `7` | `6` | 60 | START | 60 | 104 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `22` | `21` | 60 | START | 60 | 132 |
| ✅ EXACT | `Action_PullLeadBlock` | DE2 | `4` | `3` | 60 | START | 60 | 155 |
| ✅ EXACT | `Action_PlaySideFakeStep` | TE | `5` | `4` | 66 | START | 66 | 109 |
| ✅ EXACT | `Action_SnapReceive` | DT2 | `6` | `5` | 75 | END | 56 | 75 |
| ✅ EXACT | `Action_Handoff` | DT2 | `6` | `5` | 81 | START | 81 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | TE | `5` | `4` | 110 | START | 110 | 136 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 155 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 189 | 134 | inferred_complete_timeline |
| `Action_None` | 192 | 197 | 6 | inferred_complete_timeline |
| `Action_None` | 202 | 215 | 14 | inferred_complete_timeline |
| `Action_None` | 218 | 239 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 239 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 80 | 25 | inferred_complete_timeline |
| `Action_None` | 88 | 90 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 66 | 109 | 44 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 136 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 142 | 143 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 104 | 45 | inferred_complete_timeline |
| `Action_DownBlock` | 108 | 111 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 135 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 143 | 148 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 239 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 239 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 141 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 197 | 142 | inferred_complete_timeline |
| `Action_None` | 199 | 223 | 25 | inferred_complete_timeline |
| `Action_None` | 225 | 239 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 239 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 60 | 155 | 96 | inferred_complete_timeline |
| `Action_None` | 156 | 239 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 122 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_SnapReceive` | 56 | 75 | 20 | inferred_complete_timeline |
| `Action_None` | 76 | 80 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 81 | 109 | 29 | inferred_complete_timeline |
| `Action_None` | 110 | 239 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 84 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 96 | 41 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_None` | 105 | 126 | 22 | inferred_complete_timeline |
| `Action_None` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 156 | 16 | inferred_complete_timeline |
| `Action_None` | 167 | 176 | 10 | inferred_complete_timeline |
| `Action_None` | 178 | 181 | 4 | inferred_complete_timeline |
| `Action_None` | 186 | 239 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 239 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 118 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–239 | 198 | 9 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 0–132 | 133 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 123–239 | 107 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 125–239 | 104 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 126–239 | 114 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 140–239 | 99 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 145–239 | 90 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 157–239 | 67 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 161–199 | 39 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 162–163 | 2 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 177–220 | 25 | 5 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 195–218 | 19 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 208–233 | 25 | 2 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 220–221 | 2 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 316: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '18' (Unknown) duration 96 frames exceeds threshold 90 frames [start=60, end=155].
- ⚠️ Action 'Action_BallCarry' range [110-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [142-143] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [60-104] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [108-111] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-135] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [143-148] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [60-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-96] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-126] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-156] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-176] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-189] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-215] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-80] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-197] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-223] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [60-93] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [102-105] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-117] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [136-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [143-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [60-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-140] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-129] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-187] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-199] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-181] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-194] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-220] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-211] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-218] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-233] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>