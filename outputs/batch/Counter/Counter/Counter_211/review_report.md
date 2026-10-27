# Play-Annotation-Generator Annotation Review — Counter_211

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_211`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 140
- **Validation Warnings:** 155
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 120
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | RT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `3` | `2` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | FB | offense | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | RT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `10` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 72 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | RT | `13` | `12` | 73 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `20` | `19` | 76 | START | 76 | 100 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `3` | `2` | 76 | START | 76 | 125 |
| ✅ EXACT | `Action_PullBlock` | LG | `21` | `20` | 76 | START | 76 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | FB | `10` | `9` | 76 | START | 76 | 125 |
| ✅ EXACT | `Action_SnapReceive` | RT | `13` | `12` | 76 | END | 73 | 76 |
| ✅ EXACT | `Action_Handoff` | RT | `13` | `12` | 100 | START | 100 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `2` | `1` | 112 | START | 112 | 154 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 151 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 221 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_BallCarry` | 112 | 154 | 43 | inferred_complete_timeline |
| `Action_BallCarry` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 162 | 389 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 76 | 125 | 50 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 127 | 128 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 174 | 102 | inferred_complete_timeline |
| `Action_None` | 176 | 389 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 389 | 317 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 143 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–336
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PullBlock` | 76 | 151 | 76 | inferred_complete_timeline |
| `Action_None` | 152 | 295 | 144 | inferred_complete_timeline |
| `Action_None` | 297 | 308 | 12 | inferred_complete_timeline |
| `Action_None` | 311 | 315 | 5 | inferred_complete_timeline |
| `Action_None` | 317 | 329 | 13 | inferred_complete_timeline |
| `Action_None` | 331 | 332 | 2 | inferred_complete_timeline |
| `Action_None` | 334 | 336 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_DownBlock` | 76 | 100 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 106 | 121 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 129 | 134 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 136 | 151 | 16 | inferred_complete_timeline |
| `Action_None` | 152 | 389 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_SnapReceive` | 73 | 76 | 4 | inferred_complete_timeline |
| `Action_None` | 77 | 90 | 14 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 100 | 111 | 12 | inferred_complete_timeline |
| `Action_None` | 112 | 389 | 278 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 221 | 149 | inferred_complete_timeline |
| `Action_None` | 224 | 226 | 3 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_None` | 253 | 257 | 5 | inferred_complete_timeline |
| `Action_None` | 276 | 389 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 389 | 317 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 259 | 187 | inferred_complete_timeline |
| `Action_None` | 263 | 389 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–346
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 185 | 113 | inferred_complete_timeline |
| `Action_None` | 188 | 202 | 15 | inferred_complete_timeline |
| `Action_None` | 214 | 227 | 14 | inferred_complete_timeline |
| `Action_None` | 233 | 346 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 147 | 75 | inferred_complete_timeline |
| `Action_None` | 156 | 165 | 10 | inferred_complete_timeline |
| `Action_None` | 194 | 197 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 96 | 24 | inferred_complete_timeline |
| `Action_None` | 99 | 208 | 110 | inferred_complete_timeline |
| `Action_None` | 212 | 389 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–381
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 362 | 290 | inferred_complete_timeline |
| `Action_None` | 364 | 381 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 389 | 317 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 179 | 107 | inferred_complete_timeline |
| `Action_None` | 184 | 243 | 60 | inferred_complete_timeline |
| `Action_None` | 246 | 266 | 21 | inferred_complete_timeline |
| `Action_None` | 269 | 270 | 2 | inferred_complete_timeline |
| `Action_None` | 272 | 274 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 361 | 289 | inferred_complete_timeline |
| `Action_None` | 363 | 364 | 2 | inferred_complete_timeline |
| `Action_None` | 366 | 388 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 98 | 26 | inferred_complete_timeline |
| `Action_None` | 100 | 164 | 65 | inferred_complete_timeline |
| `Action_None` | 167 | 184 | 18 | inferred_complete_timeline |
| `Action_None` | 187 | 235 | 49 | inferred_complete_timeline |
| `Action_None` | 239 | 389 | 151 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–125 | 126 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–125 | 123 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 132–170 | 30 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 132–389 | 221 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 145–389 | 245 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 146–147 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 160–230 | 58 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 169–171 | 3 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 183–389 | 207 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 183–187 | 5 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 195–276 | 80 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 215–384 | 95 | 12 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 217–227 | 11 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 222–258 | 22 | 6 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 236–237 | 2 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 243–389 | 143 | 2 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 297–298 | 2 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 327–328 | 2 | 1 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 343–351 | 9 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 343–344 | 2 | 1 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 349–350 | 2 | 1 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 356–359 | 4 | 1 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 359–363 | 5 | 1 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 363–389 | 25 | 2 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 370–389 | 15 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `13` (RT)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 100 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 423: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 424: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_None' range [73-174] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [112-154] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [158-159] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [162-389] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [76-125] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-98] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-164] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-184] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-235] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-221] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-257] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-361] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-388] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [76-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [127-128] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-185] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-202] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-227] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-346] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-362] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-381] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-389] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-179] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-243] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-266] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-147] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-165] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-96] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-208] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-259] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [76-100] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [106-121] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [129-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-295] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-308] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-315] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-336] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-221] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-158] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-170] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-137] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-156] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-209] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-214] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-187] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-224] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-276] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-220] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-250] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-277] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-326] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-330] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-336] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-357] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-365] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-227] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-247] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-351] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-359] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-363] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-379] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-389] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-379] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-385] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.

</details>