# Play-Annotation-Generator Annotation Review — Counter_12

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_12`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LB1 | defense | `4` | `3` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 1 | START | 7 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 1 | START | 7 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 1 | START | 7 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 1 | START | 7 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 1 | START | 7 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `5` | `Group` | 1 | START | 7 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 1 | START | 7 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 1 | START | 7 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `9` | `Group` | 1 | START | 7 | 31 |
| ✅ EXACT | `Action_BallSnap` | LB1 | `4` | `3` | 32 | START | 32 | 48 |
| ✅ EXACT | `Action_DownBlock` | C | `14` | `13` | 37 | START | 37 | 129 |
| ✅ EXACT | `Action_DownBlock` | RT | `7` | `6` | 37 | START | 37 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `6` | `5` | 37 | START | 37 | 68 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `13` | `12` | 37 | START | 37 | 129 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 48 | END | 32 | 48 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 63 | START | 63 | 81 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `11` | `10` | 82 | START | 102 | 103 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 129 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 7–215
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 31 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 32 | 48 | 17 | inferred_complete_timeline |
| `Action_None` | 49 | 62 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 63 | 81 | 19 | inferred_complete_timeline |
| `Action_None` | 82 | 215 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 7–103
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 77 | 71 | inferred_complete_timeline |
| `Action_BallCarry` | 102 | 103 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 7–225
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 31 | 25 | inferred_complete_timeline |
| `Action_None` | 32 | 101 | 70 | inferred_complete_timeline |
| `Action_None` | 104 | 225 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 7–176
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 31 | 25 | inferred_complete_timeline |
| `Action_None` | 32 | 140 | 109 | inferred_complete_timeline |
| `Action_None` | 142 | 167 | 26 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 7–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 36 | 30 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 37 | 129 | 93 | inferred_complete_timeline |
| `Action_None` | 130 | 239 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 7–82
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 36 | 30 | inferred_complete_timeline |
| `Action_PullBlock` | 37 | 68 | 32 | inferred_complete_timeline |
| `Action_PullBlock` | 70 | 82 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 7–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 36 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 37 | 129 | 93 | inferred_complete_timeline |
| `Action_None` | 130 | 144 | 15 | inferred_complete_timeline |
| `Action_None` | 146 | 239 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 7–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 31 | 25 | inferred_complete_timeline |
| `Action_None` | 32 | 116 | 85 | inferred_complete_timeline |
| `Action_None` | 124 | 239 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 7–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 36 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 37 | 129 | 93 | inferred_complete_timeline |
| `Action_None` | 130 | 239 | 110 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 7–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 31 | 25 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 7–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 31 | 25 | inferred_complete_timeline |
| `Action_None` | 32 | 83 | 52 | inferred_complete_timeline |
| `Action_None` | 86 | 239 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 7–239
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 31 | 25 | inferred_complete_timeline |
| `Action_None` | 32 | 58 | 27 | inferred_complete_timeline |
| `Action_None` | 60 | 63 | 4 | inferred_complete_timeline |
| `Action_None` | 85 | 97 | 13 | inferred_complete_timeline |
| `Action_None` | 100 | 105 | 6 | inferred_complete_timeline |
| `Action_None` | 107 | 239 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 7–98
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 31 | 25 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 48 | 17 | inferred_complete_timeline |
| `Action_None` | 49 | 98 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 7–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 31 | 25 | inferred_complete_timeline |
| `Action_None` | 32 | 98 | 67 | inferred_complete_timeline |
| `Action_None` | 104 | 239 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 7–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 31 | 25 | inferred_complete_timeline |
| `Action_None` | 32 | 239 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 7–228
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 31 | 25 | inferred_complete_timeline |
| `Action_None` | 32 | 225 | 194 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 39–239 | 195 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 65–111 | 35 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 80–239 | 134 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 85–239 | 155 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 99–239 | 141 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 112–239 | 103 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 124–148 | 6 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 142–152 | 10 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 165–224 | 60 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 168–178 | 11 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 186–239 | 47 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 187–239 | 53 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 195–239 | 45 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 212–239 | 28 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 219–220 | 2 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 219–236 | 18 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 232–239 | 8 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 236–238 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `6` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `11` (RB): Annotated start 82 != Inferred start 102

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '6' (RT) duration 93 frames exceeds threshold 90 frames [start=37, end=129].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (C) duration 93 frames exceeds threshold 90 frames [start=37, end=129].
- ⚠️ Action 'Action_None' range [32-116] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-98] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-83] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-98] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-140] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-167] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [37-68] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [70-82] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-101] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-225] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-215] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [102-103] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-225] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [37-129] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-144] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-58] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-74] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-111] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-197] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-224] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-178] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-236] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '33' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.

</details>