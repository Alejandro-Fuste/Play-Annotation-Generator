# Play-Annotation-Generator Annotation Review — Power_267

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_267`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 479
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 51
- **Validation Warnings:** 58
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 39
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ EXACT | `Action_DownBlock` | CB5 | defense | `17` | `17` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 15 | START | 15 | 479 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 15 | START | 15 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 15 | START | 15 | 229 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `16` | `Group` | 15 | START | 15 | 479 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 15 | START | 15 | 346 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 15 | START | 15 | 388 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 15 | START | 15 | 221 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 15 | START | 15 | 221 |
| ✅ EXACT | `Action_DownBlock` | CB5 | `17` | `17` | 222 | START | 222 | 270 |
| ✅ EXACT | `Action_DownBlock` | LT | `3` | `3` | 222 | START | 222 | 270 |
| ✅ EXACT | `Action_PullBlock` | RG | `21` | `21` | 222 | START | 222 | 270 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 15–346
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 346 | 332 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 15–479
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 479 | 465 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 15–479
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 479 | 465 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 15–246
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 246 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 15–476
- **Visible Samples:** 462

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 221 | 207 | inferred_complete_timeline |
| `Action_DownBlock` | 222 | 270 | 49 | inferred_complete_timeline |
| `Action_None` | 271 | 476 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 15–445
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 229 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 445 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 15–479
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 221 | 207 | inferred_complete_timeline |
| `Action_PullBlock` | 222 | 270 | 49 | inferred_complete_timeline |
| `Action_None` | 271 | 479 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 15–388
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 388 | 374 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 15–423
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 286 | 272 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 332 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 336 | 423 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 15–479
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 479 | 465 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 15–246
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 246 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 15–445
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 279 | 265 | inferred_complete_timeline |
| `Action_PreSnap` | 285 | 445 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 15–474
- **Visible Samples:** 459

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 462 | 448 | inferred_complete_timeline |
| `Action_PreSnap` | 464 | 474 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 15–479
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 479 | 465 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 15–479
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 479 | 465 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 15–479
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 479 | 465 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 15–479
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 479 | 465 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 15–471
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 364 | 350 | inferred_complete_timeline |
| `Action_PreSnap` | 368 | 471 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 15–426
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 221 | 207 | inferred_complete_timeline |
| `Action_DownBlock` | 222 | 270 | 49 | inferred_complete_timeline |
| `Action_None` | 271 | 426 | 156 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 15–295 | 281 | 1 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 15–479 | 464 | 2 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 15–479 | 463 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 238–410 | 173 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 285–449 | 165 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 304–403 | 100 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 313–336 | 10 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 392–396 | 5 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 395–450 | 22 | 5 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 422–462 | 25 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 35 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 534: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ Row 534: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [15-295] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-286] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-332] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-423] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-476] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-246] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-472] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-364] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-471] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-361] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-279] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-445] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-246] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-462] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [464-474] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-229] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-445] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-426] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-346] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-388] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-410] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-449] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-403] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-315] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-336] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-396] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-398] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-410] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-413] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-427] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-450] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [422-430] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-436] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-453] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [461-462] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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

</details>