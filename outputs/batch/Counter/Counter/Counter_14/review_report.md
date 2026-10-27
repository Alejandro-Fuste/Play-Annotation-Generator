# Play-Annotation-Generator Annotation Review — Counter_14

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_14`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 61
- **Validation Warnings:** 47
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 40
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `6` | `5` |
| ⚠️ START CHANGED | `Action_PullBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `3` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `5` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `9` | `Group` | 0 | START | 0 | 95 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 96 | START | 96 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `14` | `13` | 102 | START | 102 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `6` | `5` | 102 | START | 102 | 124 |
| ⚠️ START CHANGED | `Action_PullBlock` | C | `15` | `14` | 102 | START | 107 | 167 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `1` | `0` | 102 | START | 102 | 167 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 106 | END | 96 | 106 |
| ✅ EXACT | `Action_BallCarry` | QB | `10` | `9` | 157 | START | 157 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 167 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_SnapReceive` | 96 | 106 | 11 | inferred_complete_timeline |
| `Action_None` | 107 | 156 | 50 | inferred_complete_timeline |
| `Action_BallCarry` | 157 | 239 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 129 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 181 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 169 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_DownBlock` | 102 | 124 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 135 | 137 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_DownBlock` | 102 | 145 | 44 | inferred_complete_timeline |
| `Action_DownBlock` | 147 | 167 | 21 | inferred_complete_timeline |
| `Action_None` | 168 | 239 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_BallSnap` | 96 | 106 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 107 | 167 | 61 | inferred_complete_timeline |
| `Action_None` | 168 | 178 | 11 | inferred_complete_timeline |
| `Action_None` | 180 | 208 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 127 | 32 | inferred_complete_timeline |
| `Action_None` | 132 | 163 | 32 | inferred_complete_timeline |
| `Action_None` | 165 | 182 | 18 | inferred_complete_timeline |
| `Action_None` | 187 | 237 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 102 | 167 | 66 | inferred_complete_timeline |
| `Action_None` | 168 | 239 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 239 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 176 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 108 | 13 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 135 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 118 | 23 | inferred_complete_timeline |
| `Action_None` | 120 | 239 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 195 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 207 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 152 | 57 | inferred_complete_timeline |
| `Action_None` | 154 | 239 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 210 | 115 | inferred_complete_timeline |
| `Action_None` | 213 | 239 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 128–233 | 105 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 135–173 | 39 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 142–168 | 27 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 179–198 | 20 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 202–239 | 29 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 216–228 | 13 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 218–221 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (2 segments found)
- ⚠️ `Action_PullBlock` for actor_track_id `15` (C): Annotated start 102 != Inferred start 107

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 31 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [96–106], lower_priority='Action_PullBlock' annotated_start=102, effective_Action_PullBlock_start=107.
- ⚠️ Action 'Action_None' range [96-152] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-181] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-207] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-129] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [102-124] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [135-137] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-210] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-169] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-195] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-163] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-182] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-237] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [102-145] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [107-167] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-178] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-208] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-137] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-233] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-173] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-198] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-219] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-228] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '23' has 2 frames without a visible bounding box.
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

</details>