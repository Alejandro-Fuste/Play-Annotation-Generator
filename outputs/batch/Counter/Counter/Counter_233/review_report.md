# Play-Annotation-Generator Annotation Review — Counter_233

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_233`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 73
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DE1 | defense | `2` | `1` |
| ✅ EXACT | `Action_PlaySideFakeStep` | CB2 | defense | `15` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | CB2 | defense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 244 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 244 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 244 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 244 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 244 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 244 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 245 | START | 245 | 263 |
| ✅ EXACT | `Action_DownBlock` | RT | `13` | `12` | 247 | START | 247 | 389 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `18` | `17` | 247 | START | 264 | 280 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `22` | `21` | 247 | START | 247 | 263 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `17` | `16` | 247 | START | 247 | 326 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DE1 | `2` | `1` | 247 | START | 247 | 341 |
| ✅ EXACT | `Action_PlaySideFakeStep` | CB2 | `15` | `14` | 250 | START | 250 | 297 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 263 | END | 245 | 263 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `10` | 278 | START | 278 | 297 |
| ✅ EXACT | `Action_BallCarry` | CB2 | `15` | `14` | 298 | START | 298 | 419 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 389 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_SnapReceive` | 245 | 263 | 19 | inferred_complete_timeline |
| `Action_None` | 264 | 277 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 278 | 297 | 20 | inferred_complete_timeline |
| `Action_None` | 298 | 419 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 419 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–353
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 346 | 102 | inferred_complete_timeline |
| `Action_None` | 348 | 353 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 419 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–350
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 317 | 73 | inferred_complete_timeline |
| `Action_None` | 322 | 325 | 4 | inferred_complete_timeline |
| `Action_None` | 334 | 350 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |
| `Action_DownBlock` | 247 | 263 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 267 | 269 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 279 | 301 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 307 | 333 | 27 | inferred_complete_timeline |
| `Action_None` | 391 | 392 | 2 | inferred_complete_timeline |
| `Action_None` | 399 | 419 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–280
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_BallSnap` | 245 | 263 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 264 | 280 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |
| `Action_PullBlock` | 247 | 326 | 80 | inferred_complete_timeline |
| `Action_PullBlock` | 332 | 336 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 339 | 389 | 51 | inferred_complete_timeline |
| `Action_None` | 390 | 419 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |
| `Action_DownBlock` | 247 | 389 | 143 | inferred_complete_timeline |
| `Action_None` | 390 | 419 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–347
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 247 | 341 | 95 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 345 | 347 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 419 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–403
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 373 | 129 | inferred_complete_timeline |
| `Action_None` | 375 | 403 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 419 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 419 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 297 | 53 | inferred_complete_timeline |
| `Action_None` | 299 | 375 | 77 | inferred_complete_timeline |
| `Action_None` | 377 | 387 | 11 | inferred_complete_timeline |
| `Action_None` | 389 | 390 | 2 | inferred_complete_timeline |
| `Action_None` | 392 | 419 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 348 | 104 | inferred_complete_timeline |
| `Action_None` | 350 | 419 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 250 | 297 | 48 | inferred_complete_timeline |
| `Action_BallCarry` | 298 | 419 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 287 | 43 | inferred_complete_timeline |
| `Action_None` | 289 | 291 | 3 | inferred_complete_timeline |
| `Action_None` | 293 | 330 | 38 | inferred_complete_timeline |
| `Action_None` | 332 | 335 | 4 | inferred_complete_timeline |
| `Action_None` | 338 | 348 | 11 | inferred_complete_timeline |
| `Action_None` | 353 | 419 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 419 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 419 | 175 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–309 | 310 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–419 | 420 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 286–419 | 119 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 299–304 | 6 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 348–383 | 36 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 353–385 | 33 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 362–388 | 24 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 377–419 | 43 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 393–419 | 27 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 400–417 | 18 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 412–419 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `18` (C): Annotated start 247 != Inferred start 264
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 468: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 468: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (RT) duration 143 frames exceeds threshold 90 frames [start=247, end=389].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '16' (RG) duration 143 frames exceeds threshold 90 frames [start=247, end=389].
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [245–263], lower_priority='Action_DownBlock' annotated_start=247, effective_Action_DownBlock_start=264.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '21' (LG) duration 143 frames exceeds threshold 90 frames [start=247, end=389].
- ⚠️ Action 'Action_None' range [245-346] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-353] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [247-341] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [345-347] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-297] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-375] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-387] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-419] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-419] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-348] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-419] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-309] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-419] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [247-389] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-419] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-373] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-403] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-317] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-350] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [247-326] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [332-336] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [264-280] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-287] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-330] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-335] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-348] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [247-263] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [267-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [279-301] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [307-333] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-381] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-409] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-419] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-304] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-383] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-385] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-382] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-388] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-417] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>