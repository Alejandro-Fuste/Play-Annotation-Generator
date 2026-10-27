# Play-Annotation-Generator Annotation Review — Counter_4

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_4`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | DT | defense | `10` | `9` |
| ⚠️ START CHANGED | `Action_DownBlock` | Position_Unknown | Team_Unknown | `19` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `2` | `1` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `1` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 79 |
| ⚠️ START CHANGED | `Action_BallSnap` | DT | `10` | `9` | 80 | START | 81 | 92 |
| ⚠️ START CHANGED | `Action_DownBlock` | Position_Unknown | `19` | `17` | 91 | START | 103 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `2` | `1` | 91 | START | 91 | 103 |
| ✅ EXACT | `Action_PullBlock` | RG | `5` | `4` | 91 | START | 91 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | `3` | `2` | 91 | START | 91 | 114 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 92 | END | 88 | 92 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `16` | 109 | START | 109 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `6` | 125 | START | 153 | 157 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 172 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 88 | 92 | 5 | inferred_complete_timeline |
| `Action_None` | 93 | 108 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 109 | 124 | 16 | inferred_complete_timeline |
| `Action_None` | 125 | 167 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_BallCarry` | 153 | 157 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 159 | 160 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 121 | 42 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 147 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 91 | 114 | 24 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 125 | 172 | 48 | inferred_complete_timeline |
| `Action_None` | 173 | 181 | 9 | inferred_complete_timeline |
| `Action_None` | 183 | 279 | 97 | inferred_complete_timeline |
| `Action_None` | 281 | 299 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 112 | 33 | inferred_complete_timeline |
| `Action_None` | 116 | 143 | 28 | inferred_complete_timeline |
| `Action_None` | 170 | 176 | 7 | inferred_complete_timeline |
| `Action_None` | 178 | 184 | 7 | inferred_complete_timeline |
| `Action_None` | 188 | 195 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_DownBlock` | 91 | 103 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 133 | 150 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 152 | 157 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 159 | 172 | 14 | inferred_complete_timeline |
| `Action_None` | 173 | 188 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PullBlock` | 91 | 172 | 82 | inferred_complete_timeline |
| `Action_None` | 173 | 236 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 143 | 64 | inferred_complete_timeline |
| `Action_None` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_None` | 156 | 183 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 92 | 13 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 97 | 104 | 8 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 181 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 93 | 14 | inferred_complete_timeline |
| `Action_None` | 102 | 109 | 8 | inferred_complete_timeline |
| `Action_None` | 120 | 150 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 57 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 81 | 92 | 12 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 108 | 117 | 10 | inferred_complete_timeline |
| `Action_None` | 120 | 140 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 110 | 31 | inferred_complete_timeline |
| `Action_None` | 112 | 120 | 9 | inferred_complete_timeline |
| `Action_None` | 130 | 139 | 10 | inferred_complete_timeline |
| `Action_None` | 144 | 174 | 31 | inferred_complete_timeline |
| `Action_None` | 189 | 214 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 125 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 223 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_None` | 80 | 111 | 32 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_None` | 137 | 152 | 16 | inferred_complete_timeline |
| `Action_None` | 154 | 201 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 79 | 51 | inferred_complete_timeline |
| `Action_None` | 80 | 295 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `19` | Position_Unknown | Team_Unknown | 13–104 | 22 | 6 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 121–244 | 124 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 154–189 | 34 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 154–159 | 6 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 163–261 | 97 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 185–207 | 16 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 277–281 | 5 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 292–299 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `10` (DT): Annotated start 80 != Inferred start 81
- ⚠️ `Action_DownBlock` for actor_track_id `19` (Position_Unknown): Annotated start 91 != Inferred start 103
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 10: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [80-121] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [91-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [133-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [152-157] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [159-172] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-188] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [91-114] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [125-172] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-181] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-279] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-223] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-236] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-125] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [153-157] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [159-160] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-112] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-143] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-184] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-195] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-143] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-183] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-57] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [81-92] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-295] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-110] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-139] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-214] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-111] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-152] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-201] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-104] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-181] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-93] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-109] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-150] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-78] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [109-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-167] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-17] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-62] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-68] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [103-104] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-244] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-185] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-261] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-192] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-281] for track '23' has 2 frames without a visible bounding box.
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

</details>