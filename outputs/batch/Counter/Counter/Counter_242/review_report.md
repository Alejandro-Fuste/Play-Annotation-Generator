# Play-Annotation-Generator Annotation Review — Counter_242

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_242`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 6
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
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `4` | `3` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `9` | `8` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 106 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 104 | START | 104 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `11` | `10` | 107 | START | 107 | 165 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `12` | `11` | 107 | START | 117 | 208 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `4` | `3` | 107 | START | 107 | 208 |
| ✅ EXACT | `Action_PullBlock` | RG | `3` | `2` | 107 | START | 107 | 208 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `9` | `8` | 107 | START | 107 | 176 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `2` | `1` | 111 | START | 111 | 150 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 116 | END | 104 | 116 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `12` | 136 | START | 136 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `2` | `1` | 151 | START | 151 | 230 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 208 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_SnapReceive` | 104 | 116 | 13 | inferred_complete_timeline |
| `Action_None` | 117 | 135 | 19 | inferred_complete_timeline |
| `Action_Handoff` | 136 | 150 | 15 | inferred_complete_timeline |
| `Action_None` | 151 | 211 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 111 | 150 | 40 | inferred_complete_timeline |
| `Action_BallCarry` | 151 | 230 | 80 | inferred_complete_timeline |
| `Action_BallCarry` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 107 | 176 | 70 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 186 | 208 | 23 | inferred_complete_timeline |
| `Action_None` | 209 | 239 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 165 | 59 | inferred_complete_timeline |
| `Action_DownBlock` | 167 | 208 | 42 | inferred_complete_timeline |
| `Action_None` | 209 | 233 | 25 | inferred_complete_timeline |
| `Action_None` | 235 | 238 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_BallSnap` | 104 | 116 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 117 | 208 | 92 | inferred_complete_timeline |
| `Action_None` | 209 | 239 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PullBlock` | 107 | 208 | 102 | inferred_complete_timeline |
| `Action_None` | 209 | 239 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 5–181
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 103 | 99 | inferred_complete_timeline |
| `Action_None` | 104 | 181 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 103 | 67 | inferred_complete_timeline |
| `Action_None` | 104 | 170 | 67 | inferred_complete_timeline |
| `Action_None` | 176 | 239 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 3–231
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 11 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 18 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 34 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 88 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 103 | 10 | inferred_complete_timeline |
| `Action_None` | 104 | 106 | 3 | inferred_complete_timeline |
| `Action_None` | 108 | 120 | 13 | inferred_complete_timeline |
| `Action_None` | 152 | 168 | 17 | inferred_complete_timeline |
| `Action_None` | 203 | 222 | 20 | inferred_complete_timeline |
| `Action_None` | 226 | 231 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 239 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 154 | 51 | inferred_complete_timeline |
| `Action_None` | 157 | 239 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 147 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 147 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–239 | 240 | 3 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–239 | 224 | 5 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 131–132 | 2 | 1 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 132–138 | 5 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 148–239 | 89 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 177–208 | 21 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 187–234 | 47 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 190–239 | 50 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 193–227 | 31 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 217–238 | 20 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (3 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `12` (C): Annotated start 107 != Inferred start 117
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 485: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '2' (RG) duration 102 frames exceeds threshold 90 frames [start=107, end=208].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '3' (Unknown) duration 102 frames exceeds threshold 90 frames [start=107, end=208].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '10' (LT) duration 102 frames exceeds threshold 90 frames [start=107, end=208].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '11' (C) duration 102 frames exceeds threshold 90 frames [start=107, end=208].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [104–116], lower_priority='Action_DownBlock' annotated_start=107, effective_Action_DownBlock_start=117.
- ⚠️ Action 'Action_None' range [104-147] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [151-230] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [107-208] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-154] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-164] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-218] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [107-176] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-147] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [107-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [167-208] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-233] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [117-208] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-211] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-11] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-18] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-34] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-88] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-222] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-103] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-181] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-155] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-191] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-218] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-234] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-205] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-227] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-233] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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

</details>