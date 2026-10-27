# Play-Annotation-Generator Annotation Review — CrackToss_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_13`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 76
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | RG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR3 | offense | `2` | `1` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | RG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 0 | START | 0 | 196 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `19` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 196 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 196 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 194 | START | 194 | 196 |
| ✅ EXACT | `Action_SnapReceive` | RG | `15` | `14` | 196 | END | 194 | 196 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | `11` | `10` | 197 | START | 197 | 265 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR3 | `2` | `1` | 197 | START | 197 | 265 |
| ✅ EXACT | `Action_PullBlock` | LT | `8` | `7` | 197 | START | 197 | 307 |
| ✅ EXACT | `Action_Toss` | RG | `15` | `14` | 203 | START | 203 | 230 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `5` | 231 | START | 231 | 355 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 307 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_BallCarry` | 231 | 355 | 125 | inferred_complete_timeline |
| `Action_BallCarry` | 358 | 359 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 265 | 72 | inferred_complete_timeline |
| `Action_None` | 281 | 359 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–348
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |
| `Action_CrackBlock` | 197 | 265 | 69 | inferred_complete_timeline |
| `Action_CrackBlock` | 283 | 298 | 16 | inferred_complete_timeline |
| `Action_CrackBlock` | 301 | 307 | 7 | inferred_complete_timeline |
| `Action_None` | 308 | 348 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |
| `Action_CrackBlock` | 197 | 265 | 69 | inferred_complete_timeline |
| `Action_CrackBlock` | 281 | 307 | 27 | inferred_complete_timeline |
| `Action_None` | 308 | 359 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 359 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |
| `Action_PullBlock` | 197 | 307 | 111 | inferred_complete_timeline |
| `Action_None` | 308 | 359 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–349
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 258 | 65 | inferred_complete_timeline |
| `Action_None` | 264 | 265 | 2 | inferred_complete_timeline |
| `Action_None` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_None` | 281 | 286 | 6 | inferred_complete_timeline |
| `Action_None` | 288 | 298 | 11 | inferred_complete_timeline |
| `Action_None` | 300 | 302 | 3 | inferred_complete_timeline |
| `Action_None` | 305 | 349 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_BallSnap` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_None` | 197 | 235 | 39 | inferred_complete_timeline |
| `Action_None` | 237 | 266 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_SnapReceive` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_None` | 197 | 202 | 6 | inferred_complete_timeline |
| `Action_Toss` | 203 | 230 | 28 | inferred_complete_timeline |
| `Action_None` | 231 | 265 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 268 | 75 | inferred_complete_timeline |
| `Action_None` | 280 | 292 | 13 | inferred_complete_timeline |
| `Action_None` | 297 | 298 | 2 | inferred_complete_timeline |
| `Action_None` | 300 | 359 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 265 | 72 | inferred_complete_timeline |
| `Action_None` | 327 | 359 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 265 | 72 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |
| `Action_None` | 281 | 359 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–327
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 265 | 72 | inferred_complete_timeline |
| `Action_None` | 280 | 327 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–331
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 225 | 32 | inferred_complete_timeline |
| `Action_None` | 234 | 265 | 32 | inferred_complete_timeline |
| `Action_None` | 280 | 289 | 10 | inferred_complete_timeline |
| `Action_None` | 291 | 331 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 246 | 53 | inferred_complete_timeline |
| `Action_None` | 249 | 253 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 259 | 66 | inferred_complete_timeline |
| `Action_None` | 261 | 265 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–342
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 342 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 359 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 359 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 312 | 119 | inferred_complete_timeline |
| `Action_None` | 315 | 359 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–353
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_None` | 194 | 269 | 76 | inferred_complete_timeline |
| `Action_None` | 272 | 353 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 2–10 | 9 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 6–10 | 5 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 6–359 | 334 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 8–9 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 13–15 | 3 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 85–87 | 3 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 91–152 | 46 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 281–359 | 79 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 281–359 | 79 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 282–359 | 78 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 285–359 | 75 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 27: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '7' (LT) duration 111 frames exceeds threshold 90 frames [start=197, end=307].
- ⚠️ Action 'Action_None' range [194-265] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [197-265] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-312] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-342] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-265] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [231-355] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [358-359] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-269] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-353] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [197-307] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-259] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-265] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [197-265] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [283-298] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-348] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-258] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-286] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-298] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-349] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-265] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-327] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-225] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-265] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-289] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-331] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-265] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-246] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-253] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-265] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-268] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-292] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-193] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-235] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-266] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-10] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-10] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-53] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-62] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-193] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-265] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-15] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-87] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-103] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-152] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-359] for track '31' has 1 frames without a visible bounding box.
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

</details>