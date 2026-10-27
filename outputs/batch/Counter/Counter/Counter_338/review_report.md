# Play-Annotation-Generator Annotation Review — Counter_338

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_338`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `16` | `15` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `3` | `2` |
| ⚠️ START CHANGED | `Action_PlaySideFakeStep` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `5` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 177 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `6` | 137 | START | 137 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `13` | `12` | 140 | START | 140 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `16` | `15` | 140 | START | 140 | 177 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `7` | `6` | 140 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `14` | `13` | 140 | START | 140 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `3` | `2` | 140 | START | 140 | 162 |
| ⚠️ START CHANGED | `Action_PlaySideFakeStep` | C | `7` | `6` | 145 | START | 151 | 262 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `1` | 150 | END | 137 | 150 |
| ✅ EXACT | `Action_Handoff` | QB | `2` | `1` | 166 | START | 166 | 185 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `7` | 186 | START | 186 | 186 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 239 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_SnapReceive` | 137 | 150 | 14 | inferred_complete_timeline |
| `Action_None` | 151 | 165 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 166 | 185 | 20 | inferred_complete_timeline |
| `Action_None` | 186 | 243 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 185 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 186 | 186 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 195 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 198 | 214 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 236 | 238 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 240 | 389 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 154 | 18 | inferred_complete_timeline |
| `Action_None` | 159 | 164 | 6 | inferred_complete_timeline |
| `Action_None` | 192 | 199 | 8 | inferred_complete_timeline |
| `Action_None` | 240 | 241 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 389 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_DownBlock` | 140 | 199 | 60 | inferred_complete_timeline |
| `Action_DownBlock` | 201 | 239 | 39 | inferred_complete_timeline |
| `Action_None` | 240 | 389 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_DownBlock` | 140 | 177 | 38 | inferred_complete_timeline |
| `Action_DownBlock` | 181 | 239 | 59 | inferred_complete_timeline |
| `Action_None` | 240 | 386 | 147 | inferred_complete_timeline |
| `Action_None` | 388 | 389 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_BallSnap` | 137 | 150 | 14 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 151 | 262 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_PullBlock` | 140 | 165 | 26 | inferred_complete_timeline |
| `Action_PullBlock` | 193 | 199 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 140 | 162 | 23 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 164 | 173 | 10 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 177 | 193 | 17 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 199 | 209 | 11 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 211 | 227 | 17 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 229 | 231 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 233 | 239 | 7 | inferred_complete_timeline |
| `Action_None` | 240 | 282 | 43 | inferred_complete_timeline |
| `Action_None` | 284 | 317 | 34 | inferred_complete_timeline |
| `Action_None` | 319 | 389 | 71 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 174 | 38 | inferred_complete_timeline |
| `Action_None` | 179 | 236 | 58 | inferred_complete_timeline |
| `Action_None` | 239 | 294 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 174 | 38 | inferred_complete_timeline |
| `Action_None` | 188 | 199 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 216 | 80 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 243 | 23 | inferred_complete_timeline |
| `Action_None` | 245 | 263 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 226 | 90 | inferred_complete_timeline |
| `Action_None` | 232 | 245 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 239 | 103 | inferred_complete_timeline |
| `Action_None` | 247 | 389 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 389 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 207 | 71 | inferred_complete_timeline |
| `Action_None` | 225 | 228 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 289 | 153 | inferred_complete_timeline |
| `Action_None` | 305 | 323 | 19 | inferred_complete_timeline |
| `Action_None` | 325 | 353 | 29 | inferred_complete_timeline |
| `Action_None` | 356 | 357 | 2 | inferred_complete_timeline |
| `Action_None` | 359 | 361 | 3 | inferred_complete_timeline |
| `Action_None` | 367 | 368 | 2 | inferred_complete_timeline |
| `Action_None` | 389 | 389 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `19` | Position_Unknown | Team_Unknown | 147–149 | 3 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 170–190 | 15 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 175–221 | 47 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 205–208 | 4 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 207–389 | 183 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 212–389 | 177 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 215–389 | 175 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 216–254 | 39 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 219–267 | 47 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 235–306 | 65 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 241–389 | 149 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 242–389 | 146 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 255–389 | 135 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 277–279 | 3 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 278–279 | 2 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 316–336 | 12 | 3 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 328–330 | 3 | 1 | Undefined position; Undefined team |
| `34` | `54` | Position_Unknown | Team_Unknown | 335–389 | 55 | 1 | Undefined position; Undefined team |
| `35` | `65` | Position_Unknown | Team_Unknown | 368–389 | 16 | 3 | Undefined position; Undefined team |
| `36` | `66` | Position_Unknown | Team_Unknown | 369–380 | 12 | 1 | Undefined position; Undefined team |
| `37` | `69` | Position_Unknown | Team_Unknown | 374–380 | 4 | 2 | Undefined position; Undefined team |
| `38` | `74` | Position_Unknown | Team_Unknown | 378–389 | 12 | 1 | Undefined position; Undefined team |
| `39` | `75` | Position_Unknown | Team_Unknown | 380–381 | 2 | 1 | Undefined position; Undefined team |
| `40` | `76` | Position_Unknown | Team_Unknown | 386–389 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `7` (C)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (7 segments found)
- ⚠️ `Action_PlaySideFakeStep` for actor_track_id `7` (C): Annotated start 145 != Inferred start 151
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [137–150], lower_priority='Action_DownBlock' annotated_start=140, effective_Action_DownBlock_start=151.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [137–150], lower_priority='Action_PlaySideFakeStep' annotated_start=145, effective_Action_PlaySideFakeStep_start=151.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (LT) duration 100 frames exceeds threshold 90 frames [start=140, end=239].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '15' (LG) duration 100 frames exceeds threshold 90 frames [start=140, end=239].
- ⚠️ Action 'Action_Handoff' range [166-185] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-243] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [140-162] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [164-173] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [177-193] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [199-209] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [211-227] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [229-231] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-282] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-317] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-289] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-323] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-353] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-361] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-389] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-226] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-245] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [151-262] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-177] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '7' starts at frame 186, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [186-186] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-195] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [198-214] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [228-229] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [236-238] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-236] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-294] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-239] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-207] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [140-199] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [201-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [140-165] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [193-199] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-216] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-243] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-263] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [140-177] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [181-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-386] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-174] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-181] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-221] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-389] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-382] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-254] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-259] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-306] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-314] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-389] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-389] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-328] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-330] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-389] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-375] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-384] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-380] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-389] for track '40' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>