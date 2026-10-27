# Play-Annotation-Generator Annotation Review — Counter_365

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_365`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 218 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 218 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `22` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 218 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `8` | `Group` | 0 | START | 0 | 215 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 216 | START | 216 | 230 |
| ✅ EXACT | `Action_DownBlock` | RT | `16` | `15` | 219 | START | 219 | 312 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `21` | `20` | 219 | START | 231 | 265 |
| ✅ EXACT | `Action_DownBlock` | LT | `4` | `3` | 219 | START | 219 | 312 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `10` | `9` | 219 | START | 219 | 267 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | `19` | `18` | 219 | START | 219 | 271 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 230 | END | 216 | 230 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `16` | 239 | START | 239 | 254 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `22` | `21` | 255 | START | 255 | 341 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 312 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_SnapReceive` | 216 | 230 | 15 | inferred_complete_timeline |
| `Action_None` | 231 | 238 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 239 | 254 | 16 | inferred_complete_timeline |
| `Action_None` | 255 | 359 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 240 | 163 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 254 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 255 | 341 | 87 | inferred_complete_timeline |
| `Action_BallCarry` | 343 | 357 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 359 | 359 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 359 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–353
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 337 | 122 | inferred_complete_timeline |
| `Action_None` | 348 | 353 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 359 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 218 | 219 | inferred_complete_timeline |
| `Action_DownBlock` | 219 | 312 | 94 | inferred_complete_timeline |
| `Action_None` | 313 | 359 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 218 | 219 | inferred_complete_timeline |
| `Action_PullBlock` | 219 | 267 | 49 | inferred_complete_timeline |
| `Action_PullBlock` | 269 | 312 | 44 | inferred_complete_timeline |
| `Action_None` | 313 | 359 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_BallSnap` | 216 | 230 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 231 | 265 | 35 | inferred_complete_timeline |
| `Action_DownBlock` | 274 | 275 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–334
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 334 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 218 | 219 | inferred_complete_timeline |
| `Action_DownBlock` | 219 | 312 | 94 | inferred_complete_timeline |
| `Action_None` | 313 | 359 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 328 | 113 | inferred_complete_timeline |
| `Action_None` | 334 | 359 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–290
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 275 | 60 | inferred_complete_timeline |
| `Action_None` | 280 | 286 | 7 | inferred_complete_timeline |
| `Action_None` | 289 | 290 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 359 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 239 | 24 | inferred_complete_timeline |
| `Action_None` | 253 | 263 | 11 | inferred_complete_timeline |
| `Action_None` | 274 | 359 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–356
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 324 | 109 | inferred_complete_timeline |
| `Action_None` | 326 | 356 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 359 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–357
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 320 | 105 | inferred_complete_timeline |
| `Action_None` | 327 | 344 | 18 | inferred_complete_timeline |
| `Action_None` | 347 | 357 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 359 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 355 | 140 | inferred_complete_timeline |
| `Action_None` | 357 | 359 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_None` | 216 | 359 | 144 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–358 | 355 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–351 | 349 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 18–24 | 7 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 46–89 | 35 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 50–61 | 12 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 177–187 | 11 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 213–239 | 9 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 252–253 | 2 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 265–271 | 6 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 284–359 | 76 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 295–346 | 45 | 4 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 297–301 | 5 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 333–352 | 20 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 350–355 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 732: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 732: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '3' (LT) duration 94 frames exceeds threshold 90 frames [start=219, end=312].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '9' (LG) duration 94 frames exceeds threshold 90 frames [start=219, end=312].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '15' (RT) duration 94 frames exceeds threshold 90 frames [start=219, end=312].
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [216–230], lower_priority='Action_DownBlock' annotated_start=219, effective_Action_DownBlock_start=231.
- ⚠️ Action 'Action_None' range [216-324] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-356] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-337] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-353] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-355] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-275] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-286] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-328] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [219-267] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [269-312] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-336] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-358] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-320] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-344] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-357] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-263] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [219-271] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [274-312] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-331] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-351] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-334] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [231-265] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [274-275] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-240] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [255-341] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [343-357] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-24] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-73] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-89] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-61] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-187] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-303] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-321] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-341] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-346] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-301] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-352] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-355] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>