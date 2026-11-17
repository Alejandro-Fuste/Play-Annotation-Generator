# Play-Annotation-Generator Annotation Review — Power_125

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_125`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 51
- **Validation Warnings:** 41
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 33
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `14` | `14` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `5` | `5` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `12` | `Group` | 15 | START | 15 | 398 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 15 | START | 15 | 350 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 15 | START | 15 | 282 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 15 | START | 15 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 15 | START | 15 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 15 | START | 15 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 15 | START | 15 | 282 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 15 | START | 15 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 15 | START | 15 | 282 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 15 | START | 15 | 419 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `14` | `14` | 283 | START | 283 | 334 |
| ✅ EXACT | `Action_DownBlock` | C | `20` | `20` | 283 | START | 283 | 360 |
| ✅ EXACT | `Action_DownBlock` | RG | `5` | `5` | 283 | START | 283 | 360 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `21` | `21` | 283 | START | 283 | 360 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 350 | 336 | inferred_complete_timeline |
| `Action_PreSnap` | 358 | 383 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 390 | 392 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 409 | 419 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 419 | 405 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 419 | 405 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 419 | 405 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 398 | 384 | inferred_complete_timeline |
| `Action_PreSnap` | 400 | 419 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 419 | 405 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 419 | 405 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 282 | 268 | inferred_complete_timeline |
| `Action_DownBlock` | 283 | 360 | 78 | inferred_complete_timeline |
| `Action_None` | 361 | 419 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 282 | 268 | inferred_complete_timeline |
| `Action_DownBlock` | 283 | 360 | 78 | inferred_complete_timeline |
| `Action_None` | 361 | 398 | 38 | inferred_complete_timeline |
| `Action_None` | 402 | 419 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 15–389
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 282 | 268 | inferred_complete_timeline |
| `Action_DownBlock` | 283 | 334 | 52 | inferred_complete_timeline |
| `Action_DownBlock` | 336 | 337 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 340 | 360 | 21 | inferred_complete_timeline |
| `Action_None` | 361 | 389 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 15–409
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 394 | 380 | inferred_complete_timeline |
| `Action_PreSnap` | 402 | 409 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 15–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 398 | 384 | inferred_complete_timeline |
| `Action_PreSnap` | 402 | 419 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 15–419
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 394 | 380 | inferred_complete_timeline |
| `Action_PreSnap` | 396 | 398 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 402 | 406 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 408 | 419 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 15–288
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 66 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 288 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 15–419
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 406 | 392 | inferred_complete_timeline |
| `Action_PreSnap` | 414 | 419 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 419 | 405 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 419 | 405 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 419 | 405 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 15–419
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 406 | 392 | inferred_complete_timeline |
| `Action_PreSnap` | 409 | 419 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 15–376
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 376 | 362 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 15–419
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 352 | 338 | inferred_complete_timeline |
| `Action_PreSnap` | 357 | 419 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 15–419 | 405 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 348–365 | 18 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 404–416 | 13 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 415–419 | 5 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 417–419 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 29 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 252: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [15-406] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-419] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-419] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-398] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-419] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-406] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-376] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-394] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-409] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-352] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-398] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-350] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-383] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-392] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [283-334] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [336-337] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-389] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-398] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-419] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-419] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-394] for track '17' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-398] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-406] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-66] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-288] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [283-360] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-365] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-416] for track '23' has 2 frames without a visible bounding box.
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

</details>