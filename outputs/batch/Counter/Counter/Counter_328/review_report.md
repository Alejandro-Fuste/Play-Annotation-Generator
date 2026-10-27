# Play-Annotation-Generator Annotation Review — Counter_328

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_328`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 157
- **Validation Warnings:** 183
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 130
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DT2 | defense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | LG | offense | `4` | `3` |
| ⚠️ START CHANGED | `Action_Handoff` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 31 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 107 | START | 107 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `11` | 110 | START | 122 | 136 |
| ✅ EXACT | `Action_DownBlock` | RT | `2` | `1` | 110 | START | 110 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `9` | `8` | 110 | START | 110 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `1` | `0` | 110 | START | 110 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DT2 | `14` | `13` | 110 | START | 110 | 145 |
| ✅ EXACT | `Action_SnapReceive` | LG | `4` | `3` | 121 | END | 107 | 121 |
| ⚠️ START CHANGED | `Action_Handoff` | QB | `5` | `4` | 138 | START | 150 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `5` | 158 | START | 159 | 160 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 203 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 134 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 150 | 157 | 8 | inferred_complete_timeline |
| `Action_None` | 158 | 329 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 171 | 173 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 184 | 223 | 40 | inferred_complete_timeline |
| `Action_BallCarry` | 226 | 229 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 231 | 251 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_None` | 134 | 143 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 109 | 74 | inferred_complete_timeline |
| `Action_DownBlock` | 110 | 145 | 36 | inferred_complete_timeline |
| `Action_DownBlock` | 147 | 150 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 155 | 160 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 162 | 173 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_SnapReceive` | 107 | 121 | 15 | inferred_complete_timeline |
| `Action_None` | 122 | 145 | 24 | inferred_complete_timeline |
| `Action_None` | 150 | 165 | 16 | inferred_complete_timeline |
| `Action_None` | 170 | 184 | 15 | inferred_complete_timeline |
| `Action_None` | 195 | 200 | 6 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 106 | 44 | inferred_complete_timeline |
| `Action_BallSnap` | 107 | 121 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 122 | 136 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 143 | 157 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 162 | 179 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 189 | 203 | 15 | inferred_complete_timeline |
| `Action_None` | 204 | 218 | 15 | inferred_complete_timeline |
| `Action_None` | 220 | 233 | 14 | inferred_complete_timeline |
| `Action_None` | 237 | 240 | 4 | inferred_complete_timeline |
| `Action_None` | 242 | 247 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_PullBlock` | 110 | 139 | 30 | inferred_complete_timeline |
| `Action_PullBlock` | 141 | 145 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 150 | 160 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 162 | 166 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 168 | 174 | 7 | inferred_complete_timeline |
| `Action_PullBlock` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 220 | 17 | inferred_complete_timeline |
| `Action_None` | 222 | 226 | 5 | inferred_complete_timeline |
| `Action_None` | 229 | 287 | 59 | inferred_complete_timeline |
| `Action_None` | 291 | 301 | 11 | inferred_complete_timeline |
| `Action_None` | 312 | 315 | 4 | inferred_complete_timeline |
| `Action_None` | 318 | 329 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 109 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 110 | 127 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 164 | 58 | inferred_complete_timeline |
| `Action_None` | 167 | 192 | 26 | inferred_complete_timeline |
| `Action_None` | 196 | 208 | 13 | inferred_complete_timeline |
| `Action_None` | 220 | 329 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 182 | 76 | inferred_complete_timeline |
| `Action_None` | 184 | 220 | 37 | inferred_complete_timeline |
| `Action_None` | 222 | 227 | 6 | inferred_complete_timeline |
| `Action_None` | 229 | 233 | 5 | inferred_complete_timeline |
| `Action_None` | 237 | 329 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 109 | 48 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 110 | 145 | 36 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 150 | 155 | 6 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 157 | 166 | 10 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 170 | 175 | 6 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 203 | 203 | 1 | inferred_complete_timeline |
| `Action_None` | 204 | 218 | 15 | inferred_complete_timeline |
| `Action_None` | 220 | 224 | 5 | inferred_complete_timeline |
| `Action_None` | 253 | 255 | 3 | inferred_complete_timeline |
| `Action_None` | 258 | 260 | 3 | inferred_complete_timeline |
| `Action_None` | 263 | 300 | 38 | inferred_complete_timeline |
| `Action_None` | 313 | 314 | 2 | inferred_complete_timeline |
| `Action_None` | 318 | 326 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 134 | 28 | inferred_complete_timeline |
| `Action_None` | 187 | 191 | 5 | inferred_complete_timeline |
| `Action_None` | 209 | 214 | 6 | inferred_complete_timeline |
| `Action_None` | 216 | 244 | 29 | inferred_complete_timeline |
| `Action_None` | 246 | 248 | 3 | inferred_complete_timeline |
| `Action_None` | 250 | 251 | 2 | inferred_complete_timeline |
| `Action_None` | 253 | 263 | 11 | inferred_complete_timeline |
| `Action_None` | 265 | 329 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 191 | 85 | inferred_complete_timeline |
| `Action_None` | 211 | 214 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–247 | 230 | 7 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 23–175 | 100 | 6 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 52–118 | 55 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 142–157 | 9 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 154–329 | 173 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 164–251 | 84 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 172–324 | 123 | 5 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 174–329 | 133 | 7 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 178–329 | 152 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 193–329 | 125 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 197–329 | 114 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 204–206 | 3 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 208–329 | 122 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 231–329 | 98 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 232–262 | 30 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 238–329 | 91 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 256–329 | 74 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 260–329 | 55 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 288–290 | 3 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 313–329 | 17 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 317–326 | 10 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 319–329 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `1` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `14` (7 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `5` (QB): Annotated start 138 != Inferred start 150
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (8 segments found)

### Track Identity Issues

- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 133 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 658: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '0' (RG) duration 94 frames exceeds threshold 90 frames [start=110, end=203].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '11' (C) duration 94 frames exceeds threshold 90 frames [start=110, end=203].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [107–121], lower_priority='Action_DownBlock' annotated_start=110, effective_Action_DownBlock_start=122.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [110-139] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [141-145] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [147-148] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [150-160] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [162-166] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [168-174] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [187-188] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-220] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-287] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-301] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [110-127] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-192] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-208] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-106] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-145] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-165] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-184] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-134] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-155] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [159-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [164-166] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [171-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [176-177] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [180-182] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [184-223] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [226-229] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [231-251] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-134] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-244] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-263] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-329] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-191] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [110-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [147-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [155-160] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [162-173] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-182] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-220] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-233] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [122-136] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [143-157] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [162-179] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-218] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-233] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-247] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-223] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-247] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [110-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [147-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [150-155] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [157-166] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [170-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [182-183] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-218] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-300] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-326] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-28] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-38] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-169] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-58] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-106] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-316] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-326] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-240] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-251] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-201] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-229] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-245] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-324] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-209] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-226] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-218] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-204] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-270] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-262] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-245] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-329] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-279] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-326] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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