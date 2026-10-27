# Play-Annotation-Generator Annotation Review — Counter_192

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_192`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 50
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | SAF2 | defense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | LB2 | defense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF2 | defense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DT1 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RB | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | LB1 | defense | `5` | `4` |
| ✅ EXACT | `Action_Handoff` | LB1 | defense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | TE | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 26 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 139 |
| ✅ EXACT | `Action_BallSnap` | SAF2 | `14` | `13` | 99 | START | 99 | 103 |
| ✅ EXACT | `Action_DownBlock` | LB2 | `10` | `9` | 104 | START | 104 | 179 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF2 | `14` | `13` | 104 | START | 104 | 117 |
| ✅ EXACT | `Action_DownBlock` | LT | `6` | `5` | 104 | START | 104 | 179 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DT1 | `11` | `10` | 104 | START | 104 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RB | `7` | `6` | 104 | START | 104 | 134 |
| ✅ EXACT | `Action_SnapReceive` | LB1 | `5` | `4` | 112 | END | 99 | 112 |
| ✅ EXACT | `Action_Handoff` | LB1 | `5` | `4` | 118 | START | 118 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | TE | `9` | `8` | 140 | START | 140 | 141 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 179 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 26–139
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 98 | 73 | inferred_complete_timeline |
| `Action_None` | 99 | 139 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 104 | 134 | 31 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 136 | 153 | 18 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 162 | 179 | 18 | inferred_complete_timeline |
| `Action_None` | 180 | 233 | 54 | inferred_complete_timeline |
| `Action_None` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 175 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 269 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_BallCarry` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 143 | 268 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_DownBlock` | 104 | 179 | 76 | inferred_complete_timeline |
| `Action_None` | 180 | 269 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 128–269
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 128 | 140 | 13 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 269 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 170 | 72 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 269 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PullBlock` | 104 | 115 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 117 | 130 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 132 | 179 | 48 | inferred_complete_timeline |
| `Action_None` | 180 | 183 | 4 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 269 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 150–269
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 150 | 269 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_SnapReceive` | 99 | 112 | 14 | inferred_complete_timeline |
| `Action_None` | 113 | 117 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 118 | 139 | 22 | inferred_complete_timeline |
| `Action_None` | 140 | 269 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_DownBlock` | 104 | 179 | 76 | inferred_complete_timeline |
| `Action_None` | 180 | 269 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 135 | 37 | inferred_complete_timeline |
| `Action_None` | 137 | 151 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 269 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 116–269
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 116 | 132 | 17 | inferred_complete_timeline |
| `Action_None` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_None` | 159 | 269 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 176 | 78 | inferred_complete_timeline |
| `Action_None` | 180 | 269 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_BallSnap` | 99 | 103 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 104 | 117 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 167 | 179 | 13 | inferred_complete_timeline |
| `Action_None` | 180 | 269 | 90 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–117 | 118 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 166–269 | 95 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 213–269 | 56 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 237–269 | 33 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 240–269 | 30 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 251–269 | 19 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 258–269 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 28 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 386: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 386: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ Track ID '22' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [99-176] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-175] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-135] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-151] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [104-134] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [136-153] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-233] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [140-141] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [143-268] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [104-115] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [117-130] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-170] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [104-117] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-139] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-140] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-269] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-258] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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