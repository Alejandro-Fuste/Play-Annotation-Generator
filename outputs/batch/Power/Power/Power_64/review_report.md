# Play-Annotation-Generator Annotation Review — Power_64

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_64`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 43
- **Validation Warnings:** 60
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
- **Inferred Coverage Segments (Action_None):** 30
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 24 | START | 24 | 372 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 24 | START | 24 | 311 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 24 | START | 24 | 347 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 24 | START | 24 | 331 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 24 | START | 24 | 257 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 24 | START | 24 | 257 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 24 | START | 24 | 257 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 24 | START | 24 | 396 |
| ✅ EXACT | `Action_DownBlock` | LT | `4` | `4` | 258 | START | 258 | 306 |
| ✅ EXACT | `Action_DownBlock` | LG | `7` | `7` | 258 | START | 258 | 306 |
| ✅ EXACT | `Action_PullBlock` | RG | `6` | `6` | 258 | START | 258 | 286 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 24–331
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 331 | 308 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 24–372
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 372 | 349 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 24–396
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 396 | 373 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 24–353
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 257 | 234 | inferred_complete_timeline |
| `Action_DownBlock` | 258 | 306 | 49 | inferred_complete_timeline |
| `Action_None` | 307 | 353 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 24–351
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 257 | 234 | inferred_complete_timeline |
| `Action_DownBlock` | 258 | 306 | 49 | inferred_complete_timeline |
| `Action_None` | 307 | 351 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 24–349
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 311 | 288 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 332 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 334 | 349 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 24–286
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 257 | 234 | inferred_complete_timeline |
| `Action_PullBlock` | 258 | 286 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 24–347
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 347 | 324 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 24–350
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 166 | 143 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 319 | 152 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 323 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 327 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 334 | 335 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 344 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 350 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 24–347
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 347 | 324 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 24–350
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 350 | 327 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 24–352
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 352 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 162–201
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 162 | 186 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 201 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 24–348
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 348 | 325 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 24–419 | 396 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 24–419 | 396 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 136–235 | 100 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 181–238 | 58 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 270–272 | 3 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 285–314 | 24 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 299–303 | 5 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 311–419 | 109 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 314–419 | 106 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 361–419 | 59 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 364–419 | 56 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 394–396 | 3 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 415–416 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 33 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [24-372] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-348] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-331] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-353] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-347] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [258-286] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-351] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-396] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-352] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-311] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-332] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-349] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-347] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-350] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-319] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-323] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-327] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-335] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-344] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-350] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-235] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-186] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-201] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-238] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-272] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-300] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-308] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-314] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-303] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-419] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-396] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-416] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>