# Play-Annotation-Generator Annotation Review — Counter_144

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_144`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 176 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 177 | START | 177 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `12` | 181 | START | 194 | 200 |
| ✅ EXACT | `Action_DownBlock` | LT | `8` | `7` | 181 | START | 181 | 264 |
| ✅ EXACT | `Action_PullBlock` | RG | `4` | `3` | 181 | START | 181 | 264 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `3` | `2` | 181 | START | 181 | 257 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 193 | END | 177 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `6` | `5` | 214 | START | 214 | 259 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 264 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_SnapReceive` | 177 | 193 | 17 | inferred_complete_timeline |
| `Action_None` | 194 | 213 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 214 | 259 | 46 | inferred_complete_timeline |
| `Action_BallCarry` | 261 | 329 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 112 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 181 | 257 | 77 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 261 | 264 | 4 | inferred_complete_timeline |
| `Action_None` | 265 | 329 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 180 | 109 | inferred_complete_timeline |
| `Action_DownBlock` | 181 | 264 | 84 | inferred_complete_timeline |
| `Action_None` | 265 | 329 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 176 | 120 | inferred_complete_timeline |
| `Action_BallSnap` | 177 | 193 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 194 | 200 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 205 | 264 | 60 | inferred_complete_timeline |
| `Action_None` | 265 | 329 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_PullBlock` | 181 | 264 | 84 | inferred_complete_timeline |
| `Action_None` | 265 | 329 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 241 | 65 | inferred_complete_timeline |
| `Action_None` | 249 | 252 | 4 | inferred_complete_timeline |
| `Action_None` | 255 | 259 | 5 | inferred_complete_timeline |
| `Action_None` | 263 | 329 | 67 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 234 | 58 | inferred_complete_timeline |
| `Action_None` | 248 | 264 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 189 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 188 | 12 | inferred_complete_timeline |
| `Action_None` | 193 | 200 | 8 | inferred_complete_timeline |
| `Action_None` | 215 | 218 | 4 | inferred_complete_timeline |
| `Action_None` | 224 | 227 | 4 | inferred_complete_timeline |
| `Action_None` | 234 | 238 | 5 | inferred_complete_timeline |
| `Action_None` | 240 | 241 | 2 | inferred_complete_timeline |
| `Action_None` | 246 | 251 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 180 | 4 | inferred_complete_timeline |
| `Action_None` | 182 | 191 | 10 | inferred_complete_timeline |
| `Action_None` | 198 | 205 | 8 | inferred_complete_timeline |
| `Action_None` | 221 | 329 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 241 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 139 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 155 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 164 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 171 | 3 | inferred_complete_timeline |
| `Action_None` | 179 | 329 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `21`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 209–214
- **Visible Samples:** 6

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 209 | 214 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–225 | 222 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 86–180 | 40 | 4 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 213–234 | 22 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 227–329 | 93 | 3 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 229–245 | 12 | 3 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 230–329 | 100 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 247–285 | 34 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 247–329 | 82 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 262–329 | 68 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 262–329 | 68 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 269–329 | 58 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 277–329 | 53 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 285–329 | 45 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 305–329 | 25 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 319–327 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `21`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [177–193], lower_priority='Action_DownBlock' annotated_start=181, effective_Action_DownBlock_start=194.
- ⚠️ Action 'Action_PreSnap' range [0-176] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-207] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-221] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-241] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [181-257] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-112] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [214-259] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [261-329] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-139] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-155] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-164] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [181-264] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-241] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-259] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-134] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-157] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-234] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-264] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [194-200] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-188] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-200] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-251] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-189] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-176] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-205] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-120] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-149] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-234] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-269] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-284] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-234] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-274] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-285] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-258] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-329] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-292] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>