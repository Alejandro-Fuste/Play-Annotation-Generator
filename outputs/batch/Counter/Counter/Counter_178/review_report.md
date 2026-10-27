# Play-Annotation-Generator Annotation Review — Counter_178

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_178`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LT | offense | `15` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `15` | `13` |
| ✅ EXACT | `Action_DownBlock` | WR2 | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | CB2 | defense | `10` | `9` |
| ✅ EXACT | `Action_PullLeadBlock` | LB2 | defense | `5` | `4` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | DE2 | defense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RT | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 15 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `18` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `21` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `22` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 105 |
| ✅ EXACT | `Action_BallSnap` | LT | `15` | `13` | 159 | START | 159 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `15` | `13` | 163 | START | 163 | 172 |
| ✅ EXACT | `Action_DownBlock` | WR2 | `4` | `3` | 163 | START | 163 | 246 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | CB2 | `10` | `9` | 163 | START | 163 | 183 |
| ✅ EXACT | `Action_PullLeadBlock` | LB2 | `5` | `4` | 163 | START | 163 | 246 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RT | `6` | `5` | 168 | START | 168 | 197 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `7` | `6` | 171 | END | 159 | 171 |
| ✅ EXACT | `Action_Handoff` | DE2 | `7` | `6` | 187 | START | 187 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RT | `6` | `5` | 200 | START | 200 | 253 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 246 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 132 | 14 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 177 | 179 | 3 | inferred_complete_timeline |
| `Action_None` | 182 | 186 | 5 | inferred_complete_timeline |
| `Action_None` | 188 | 214 | 27 | inferred_complete_timeline |
| `Action_None` | 219 | 256 | 38 | inferred_complete_timeline |
| `Action_None` | 263 | 294 | 32 | inferred_complete_timeline |
| `Action_None` | 313 | 329 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 218–295
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 218 | 248 | 31 | inferred_complete_timeline |
| `Action_None` | 294 | 295 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 167 | 9 | inferred_complete_timeline |
| `Action_None` | 178 | 187 | 10 | inferred_complete_timeline |
| `Action_None` | 195 | 198 | 4 | inferred_complete_timeline |
| `Action_None` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 214 | 8 | inferred_complete_timeline |
| `Action_None` | 238 | 242 | 5 | inferred_complete_timeline |
| `Action_None` | 245 | 253 | 9 | inferred_complete_timeline |
| `Action_None` | 260 | 294 | 35 | inferred_complete_timeline |
| `Action_None` | 296 | 298 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_DownBlock` | 163 | 246 | 84 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 252 | 279 | 28 | inferred_complete_timeline |
| `Action_None` | 281 | 283 | 3 | inferred_complete_timeline |
| `Action_None` | 285 | 290 | 6 | inferred_complete_timeline |
| `Action_None` | 292 | 299 | 8 | inferred_complete_timeline |
| `Action_None` | 301 | 329 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `19`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 196–329
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 196 | 329 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–263
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 263 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 15–182
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 79 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 106 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 158 | 23 | inferred_complete_timeline |
| `Action_BallSnap` | 159 | 162 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 163 | 172 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 178 | 182 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 240–329
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 240 | 242 | 3 | inferred_complete_timeline |
| `Action_None` | 273 | 329 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 210–288
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 210 | 288 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 187–329
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 187 | 208 | 22 | inferred_complete_timeline |
| `Action_None` | 219 | 329 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 168 | 197 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 200 | 253 | 54 | inferred_complete_timeline |
| `Action_BallCarry` | 256 | 297 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 193 | 35 | inferred_complete_timeline |
| `Action_None` | 195 | 205 | 11 | inferred_complete_timeline |
| `Action_None` | 208 | 290 | 83 | inferred_complete_timeline |
| `Action_None` | 298 | 325 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_SnapReceive` | 159 | 171 | 13 | inferred_complete_timeline |
| `Action_None` | 172 | 186 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 187 | 199 | 13 | inferred_complete_timeline |
| `Action_None` | 200 | 200 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 22 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 55 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 158 | 93 | inferred_complete_timeline |
| `Action_None` | 159 | 182 | 24 | inferred_complete_timeline |
| `Action_None` | 262 | 265 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 237 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 220 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 163 | 246 | 84 | inferred_complete_timeline |
| `Action_None` | 247 | 329 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 114 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 158 | 43 | inferred_complete_timeline |
| `Action_None` | 159 | 178 | 20 | inferred_complete_timeline |
| `Action_None` | 181 | 187 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_PullBlock` | 163 | 183 | 21 | inferred_complete_timeline |
| `Action_PullBlock` | 192 | 240 | 49 | inferred_complete_timeline |
| `Action_None` | 250 | 303 | 54 | inferred_complete_timeline |
| `Action_None` | 307 | 329 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 66–329
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 66 | 158 | 93 | inferred_complete_timeline |
| `Action_None` | 159 | 207 | 49 | inferred_complete_timeline |
| `Action_None` | 209 | 329 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 185–191
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 185 | 191 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `23` | Position_Unknown | Team_Unknown | 261–329 | 61 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 265–329 | 55 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 271–329 | 59 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 272–276 | 5 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 279–281 | 3 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 282–329 | 48 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 283–285 | 3 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 290–329 | 38 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 290–295 | 6 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 303–329 | 27 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 310–329 | 20 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 310–329 | 19 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 323–329 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '14' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-158] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-167] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-187] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-214] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-242] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-253] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-294] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-237] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-193] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-205] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-290] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-325] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-279] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-290] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-299] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-329] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [168-197] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [200-253] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [256-297] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '6' starts at frame 200, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [200-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-220] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-132] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-214] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-256] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-294] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [163-183] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [192-240] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-303] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-22] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-55] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-182] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-265] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-114] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-158] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-187] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-263] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-79] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-158] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [163-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [178-182] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-207] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-208] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-329] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-288] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-248] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-271] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-275] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-324] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-295] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-329] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-314] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-329] for track '32' has 1 frames without a visible bounding box.
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