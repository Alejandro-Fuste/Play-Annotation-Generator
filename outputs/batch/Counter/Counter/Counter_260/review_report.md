# Play-Annotation-Generator Annotation Review — Counter_260

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_260`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 71
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `5` | `4` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DT1 | defense | `14` | `13` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 62 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 60 | START | 60 | 76 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `11` | `10` | 63 | START | 81 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `5` | `4` | 63 | START | 63 | 121 |
| ✅ EXACT | `Action_DownBlock` | LT | `6` | `5` | 63 | START | 63 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DT1 | `14` | `13` | 63 | START | 63 | 71 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `3` | `2` | 63 | START | 63 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `15` | `14` | 76 | END | 60 | 74 |
| ✅ EXACT | `Action_BallCarry` | QB | `15` | `14` | 108 | START | 108 | 225 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 145 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–225
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 59 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 60 | 74 | 15 | inferred_complete_timeline |
| `Action_SnapReceive` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_None` | 77 | 107 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 108 | 225 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 117 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 63 | 112 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_DownBlock` | 63 | 98 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_DownBlock` | 63 | 121 | 59 | inferred_complete_timeline |
| `Action_DownBlock` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 131 | 145 | 15 | inferred_complete_timeline |
| `Action_None` | 146 | 239 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 59 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 60 | 76 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 81 | 145 | 65 | inferred_complete_timeline |
| `Action_None` | 146 | 155 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 84 | 25 | inferred_complete_timeline |
| `Action_None` | 90 | 92 | 3 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 164 | 105 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 110 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 149 | 90 | inferred_complete_timeline |
| `Action_None` | 201 | 239 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PullBlock` | 63 | 71 | 9 | inferred_complete_timeline |
| `Action_PullBlock` | 98 | 99 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 68 | 9 | inferred_complete_timeline |
| `Action_None` | 73 | 77 | 5 | inferred_complete_timeline |
| `Action_None` | 84 | 152 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 105 | 46 | inferred_complete_timeline |
| `Action_None` | 110 | 126 | 17 | inferred_complete_timeline |
| `Action_None` | 141 | 146 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 127 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 139 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `18` | Position_Unknown | Team_Unknown | 90–134 | 45 | 1 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 92–142 | 35 | 2 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 107–142 | 36 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 127–130 | 4 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 139–144 | 6 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 152–239 | 86 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 155–239 | 85 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 176–239 | 64 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 178–209 | 31 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 188–205 | 17 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 198–239 | 42 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 198–237 | 40 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 210–214 | 5 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 211–239 | 29 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 217–239 | 23 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 227–239 | 13 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 230–239 | 10 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `11` (C): Annotated start 63 != Inferred start 81
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [60–76], lower_priority='Action_DownBlock' annotated_start=63, effective_Action_DownBlock_start=77.
- ⚠️ Action 'Action_None' range [60-84] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-105] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-126] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-146] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [63-112] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-117] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [63-121] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [128-129] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [63-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-127] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-164] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [60-76] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [81-145] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-155] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-68] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-152] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [63-71] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [98-99] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [60-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [108-225] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-134] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-142] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-142] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-209] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-195] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-205] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-237] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-214] for track '27' has 2 frames without a visible bounding box.
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