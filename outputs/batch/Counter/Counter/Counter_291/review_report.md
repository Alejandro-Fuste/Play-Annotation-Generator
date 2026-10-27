# Play-Annotation-Generator Annotation Review — Counter_291

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_291`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | RB2 | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | RB2 | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 10 | START | 10 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `12` | `Group` | 10 | START | 10 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `15` | `Group` | 10 | START | 10 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `16` | `Group` | 10 | START | 10 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 10 | START | 10 | 205 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `2` | `Group` | 10 | START | 10 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 10 | START | 10 | 205 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 10 | START | 10 | 250 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `24` | `Group` | 10 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 10 | START | 10 | 202 |
| ✅ EXACT | `Action_BallSnap` | C | `6` | `5` | 203 | START | 203 | 215 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `18` | `17` | 206 | START | 206 | 282 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `20` | `19` | 206 | START | 206 | 229 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `6` | `5` | 206 | START | 216 | 225 |
| ✅ EXACT | `Action_PullBlock` | RG | `19` | `18` | 206 | START | 206 | 305 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | `21` | `20` | 206 | START | 206 | 286 |
| ✅ EXACT | `Action_SnapReceive` | RB2 | `15` | `14` | 215 | END | 203 | 215 |
| ✅ EXACT | `Action_Handoff` | RB2 | `15` | `14` | 230 | START | 230 | 250 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `22` | `21` | 251 | START | 251 | 386 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 305 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 10–449
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 250 | 241 | inferred_complete_timeline |
| `Action_BallCarry` | 251 | 386 | 136 | inferred_complete_timeline |
| `Action_BallCarry` | 388 | 394 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 398 | 431 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 439 | 440 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 443 | 449 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 10–291
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_None` | 203 | 291 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 10–449
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_SnapReceive` | 203 | 215 | 13 | inferred_complete_timeline |
| `Action_None` | 216 | 229 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 230 | 250 | 21 | inferred_complete_timeline |
| `Action_None` | 251 | 258 | 8 | inferred_complete_timeline |
| `Action_None` | 261 | 335 | 75 | inferred_complete_timeline |
| `Action_None` | 338 | 449 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 10–449
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_None` | 203 | 449 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 10–449
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_None` | 203 | 449 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 268–269
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 10–449
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 205 | 196 | inferred_complete_timeline |
| `Action_DownBlock` | 206 | 229 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 233 | 246 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 257 | 305 | 49 | inferred_complete_timeline |
| `Action_None` | 306 | 449 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 10–449
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_BallSnap` | 203 | 215 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 216 | 225 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 227 | 233 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 242 | 298 | 57 | inferred_complete_timeline |
| `Action_DownBlock` | 301 | 305 | 5 | inferred_complete_timeline |
| `Action_None` | 306 | 449 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 10–446
- **Visible Samples:** 431

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 205 | 196 | inferred_complete_timeline |
| `Action_PullBlock` | 206 | 305 | 100 | inferred_complete_timeline |
| `Action_None` | 306 | 428 | 123 | inferred_complete_timeline |
| `Action_None` | 435 | 446 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 10–449
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_None` | 203 | 449 | 247 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 10–281
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_None` | 203 | 273 | 71 | inferred_complete_timeline |
| `Action_None` | 275 | 281 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 10–449
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_None` | 203 | 449 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 10–449
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_None` | 203 | 272 | 70 | inferred_complete_timeline |
| `Action_None` | 274 | 449 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 10–261
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_None` | 203 | 261 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 10–449
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_None` | 203 | 324 | 122 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |
| `Action_None` | 331 | 337 | 7 | inferred_complete_timeline |
| `Action_None` | 339 | 385 | 47 | inferred_complete_timeline |
| `Action_None` | 389 | 449 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 10–449
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_None` | 203 | 449 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 10–301
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_None` | 203 | 295 | 93 | inferred_complete_timeline |
| `Action_None` | 298 | 301 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 10–411
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_None` | 203 | 411 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 10–449
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_None` | 203 | 449 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>SAF4 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 10–449
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_None` | 203 | 449 | 247 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 10–449 | 440 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 10–449 | 436 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 10–323 | 311 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 266–419 | 154 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 280–449 | 168 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 299–300 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 309–449 | 136 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 316–449 | 101 | 7 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 319–321 | 3 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 322–323 | 2 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 339–340 | 2 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 390–391 | 2 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 399–449 | 51 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 401–405 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF4` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF3` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 583: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
- ⚠️ Row 584: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '5' (C) duration 100 frames exceeds threshold 90 frames [start=206, end=305].
- ⚠️ Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [203–215], lower_priority='Action_DownBlock' annotated_start=206, effective_Action_DownBlock_start=216.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '17' (Unknown) duration 100 frames exceeds threshold 90 frames [start=206, end=305].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '18' (RG) duration 100 frames exceeds threshold 90 frames [start=206, end=305].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (LG) duration 100 frames exceeds threshold 90 frames [start=206, end=305].
- ⚠️ Action 'Action_None' range [203-272] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-295] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-301] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [216-225] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [227-233] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [242-298] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-411] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-324] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-337] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-385] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-261] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-449] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-291] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-258] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-335] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-273] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-281] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [206-282] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [206-305] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-428] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-446] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [206-229] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [233-246] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [206-286] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-323] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [251-386] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [388-394] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [398-431] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [439-440] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [443-449] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-419] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-410] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-449] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-389] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-416] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-405] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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