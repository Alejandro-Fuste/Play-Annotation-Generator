# Play-Annotation-Generator Annotation Review — Counter_217

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_217`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 82
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
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 198 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 198 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 198 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 198 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 198 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 198 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 200 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 199 | START | 199 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `21` | `20` | 201 | START | 201 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `22` | `21` | 201 | START | 211 | 225 |
| ✅ EXACT | `Action_DownBlock` | LT | `8` | `7` | 201 | START | 201 | 290 |
| ✅ EXACT | `Action_PullBlock` | RG | `20` | `19` | 201 | START | 201 | 290 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `3` | `2` | 201 | START | 201 | 242 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 210 | END | 199 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `17` | `16` | 228 | START | 228 | 287 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 290 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–313
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_SnapReceive` | 199 | 210 | 12 | inferred_complete_timeline |
| `Action_None` | 211 | 227 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 228 | 287 | 60 | inferred_complete_timeline |
| `Action_BallCarry` | 293 | 313 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–304
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 304 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–317
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 317 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–398
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 398 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 299 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–415
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 201 | 242 | 42 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 244 | 290 | 47 | inferred_complete_timeline |
| `Action_None` | 291 | 325 | 35 | inferred_complete_timeline |
| `Action_None` | 331 | 415 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–384
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_DownBlock` | 201 | 290 | 90 | inferred_complete_timeline |
| `Action_None` | 291 | 384 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–317
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_DownBlock` | 201 | 210 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 222 | 227 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 233 | 290 | 58 | inferred_complete_timeline |
| `Action_None` | 291 | 317 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 198 | 110 | inferred_complete_timeline |
| `Action_BallSnap` | 199 | 210 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 211 | 225 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 227 | 290 | 64 | inferred_complete_timeline |
| `Action_None` | 291 | 419 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–311
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_PullBlock` | 201 | 290 | 90 | inferred_complete_timeline |
| `Action_None` | 291 | 311 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–326
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 220 | 22 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 272 | 44 | inferred_complete_timeline |
| `Action_None` | 277 | 294 | 18 | inferred_complete_timeline |
| `Action_None` | 298 | 326 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–306
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 274 | 76 | inferred_complete_timeline |
| `Action_None` | 298 | 300 | 3 | inferred_complete_timeline |
| `Action_None` | 304 | 306 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–311
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 236 | 38 | inferred_complete_timeline |
| `Action_None` | 242 | 252 | 11 | inferred_complete_timeline |
| `Action_None` | 256 | 270 | 15 | inferred_complete_timeline |
| `Action_None` | 274 | 311 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 234 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 234 | 36 | inferred_complete_timeline |
| `Action_None` | 236 | 247 | 12 | inferred_complete_timeline |
| `Action_None` | 249 | 270 | 22 | inferred_complete_timeline |
| `Action_None` | 274 | 294 | 21 | inferred_complete_timeline |
| `Action_None` | 297 | 319 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 394 | 196 | inferred_complete_timeline |
| `Action_None` | 402 | 419 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 419 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 319 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–356
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 276 | 78 | inferred_complete_timeline |
| `Action_None` | 281 | 356 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 293 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 419 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_None` | 199 | 419 | 221 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 220–381 | 156 | 4 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 246–278 | 21 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 246–371 | 106 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 257–281 | 8 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 311–318 | 8 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 347–350 | 4 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 376–390 | 12 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 383–384 | 2 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 385–386 | 2 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 388–389 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [199–210], lower_priority='Action_DownBlock' annotated_start=201, effective_Action_DownBlock_start=211.
- ⚠️ Action 'Action_None' range [199-274] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-300] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-306] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [201-242] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-325] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-415] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-317] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-398] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [201-290] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-384] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-234] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-293] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-394] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-236] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-252] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-270] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-311] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-319] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-304] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-276] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-356] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-220] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-272] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-294] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-326] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [228-287] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [293-313] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-234] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-247] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-270] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-294] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-319] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-311] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [201-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [222-227] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-317] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-198] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [211-225] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-419] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-235] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-246] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-265] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-381] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-264] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-352] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-371] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-281] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-318] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-350] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-381] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-390] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '31' has 1 frames without a visible bounding box.
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