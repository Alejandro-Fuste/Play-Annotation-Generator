# Play-Annotation-Generator Annotation Review — Counter_359

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_359`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 76
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `20` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 143 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 141 | START | 141 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `18` | `17` | 144 | START | 159 | 161 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `21` | `20` | 144 | START | 144 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `22` | `21` | 144 | START | 144 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `19` | `18` | 144 | START | 144 | 190 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `7` | `6` | 144 | START | 144 | 225 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 158 | END | 141 | 158 |
| ✅ EXACT | `Action_BallCarry` | QB | `17` | `16` | 187 | START | 187 | 247 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 225 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–247
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_SnapReceive` | 141 | 158 | 18 | inferred_complete_timeline |
| `Action_None` | 159 | 186 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 187 | 247 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 307 | 167 | inferred_complete_timeline |
| `Action_None` | 314 | 329 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 329 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 289 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 236 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–276
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 276 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 144 | 225 | 82 | inferred_complete_timeline |
| `Action_None` | 226 | 329 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_PullBlock` | 144 | 190 | 47 | inferred_complete_timeline |
| `Action_PullBlock` | 213 | 214 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_BallSnap` | 141 | 158 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 159 | 161 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 174 | 204 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 206 | 212 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 214 | 225 | 12 | inferred_complete_timeline |
| `Action_None` | 226 | 270 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_DownBlock` | 144 | 149 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 158 | 162 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 167 | 180 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 186 | 196 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 201 | 204 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_DownBlock` | 144 | 194 | 51 | inferred_complete_timeline |
| `Action_DownBlock` | 198 | 225 | 28 | inferred_complete_timeline |
| `Action_None` | 226 | 278 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 218 | 78 | inferred_complete_timeline |
| `Action_None` | 229 | 329 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 262 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 219 | 79 | inferred_complete_timeline |
| `Action_None` | 232 | 233 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 275 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 233 | 93 | inferred_complete_timeline |
| `Action_None` | 235 | 238 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 266 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 329 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 294 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 239 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 226 | 86 | inferred_complete_timeline |
| `Action_None` | 231 | 329 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–285
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 285 | 145 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–329 | 330 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 189–268 | 50 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 191–206 | 4 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 201–261 | 61 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 206–229 | 24 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 236–271 | 31 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 247–268 | 22 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 263–270 | 8 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 288–329 | 40 | 2 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 319–323 | 5 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 323–329 | 7 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (7 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 720: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [141–158], lower_priority='Action_DownBlock' annotated_start=144, effective_Action_DownBlock_start=159.
- ⚠️ Action 'Action_None' range [141-236] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-266] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-289] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-294] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-285] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-262] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-226] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-218] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-307] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-329] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-233] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-219] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-275] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [187-247] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [159-161] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [174-204] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [206-212] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-270] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [144-190] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [213-214] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-276] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [144-149] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [158-162] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [167-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [186-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [201-204] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [144-194] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-278] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-203] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-253] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-268] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-261] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-229] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-240] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-271] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-268] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-270] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-323] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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