# Play-Annotation-Generator Annotation Review — Power_169

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_169`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 419
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 46
- **Validation Warnings:** 37
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 26
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `17` | `17` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `3` | `3` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 27 | START | 27 | 392 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 27 | START | 27 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 27 | START | 27 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 27 | START | 27 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 27 | START | 27 | 310 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 27 | START | 27 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 27 | START | 27 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 27 | START | 27 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 27 | START | 27 | 418 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 27 | START | 27 | 246 |
| ✅ EXACT | `Action_DownBlock` | LT | `17` | `17` | 247 | START | 247 | 264 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `3` | `3` | 247 | START | 247 | 318 |
| ✅ EXACT | `Action_PullBlock` | RG | `6` | `6` | 247 | START | 247 | 318 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 27–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 419 | 393 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 27–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 419 | 393 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 27–418
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 418 | 392 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 27–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 419 | 393 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 27–392
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 392 | 366 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 27–419
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 310 | 284 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 318 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 343 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 352 | 353 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 355 | 415 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 417 | 419 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 27–264
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 246 | 220 | inferred_complete_timeline |
| `Action_DownBlock` | 247 | 264 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 27–419
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 299 | 273 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 307 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 419 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 27–412
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 246 | 220 | inferred_complete_timeline |
| `Action_PullBlock` | 247 | 318 | 72 | inferred_complete_timeline |
| `Action_None` | 319 | 412 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 27–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 419 | 393 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 27–334
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 302 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 334 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 27–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 419 | 393 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 27–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 419 | 393 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 27–313
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 313 | 287 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 27–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 419 | 393 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 27–419
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 340 | 314 | inferred_complete_timeline |
| `Action_PreSnap` | 346 | 348 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 351 | 419 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 27–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 419 | 393 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 27–419
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 337 | 311 | inferred_complete_timeline |
| `Action_PreSnap` | 340 | 344 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 419 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 27–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 419 | 393 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 27–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 419 | 393 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 27–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 419 | 393 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 27–397 | 371 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 291–419 | 127 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 347–419 | 71 | 3 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 355–399 | 35 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 27 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 340: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [27-392] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-419] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-397] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-418] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-412] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-313] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-340] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-348] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-337] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-344] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-310] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-318] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-343] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-353] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-415] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [247-264] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-302] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-334] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-307] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-419] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-305] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-419] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-348] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-363] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-359] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-399] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.

</details>