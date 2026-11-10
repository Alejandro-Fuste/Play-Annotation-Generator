# Play-Annotation-Generator Annotation Review — RPO_36

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_36`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 71
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `8` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 0 | START | 0 | 208 |
| ✅ EXACT | `Action_ZoneBlock` | C | `13` | `13` | 210 | START | 210 | 284 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `15` | `15` | 210 | START | 210 | 326 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `17` | 210 | START | 210 | 326 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `18` | 210 | START | 210 | 282 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `20` | `20` | 210 | START | 210 | 326 |
| ✅ EXACT | `Action_ReadDefender` | QB | `19` | `19` | 213 | START | 213 | 297 |
| ✅ EXACT | `Action_PullBall` | QB | `19` | `19` | 298 | START | 298 | 305 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 318 | START | 318 | 326 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–375
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 212 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 213 | 297 | 85 | inferred_complete_timeline |
| `Action_PullBall` | 298 | 305 | 8 | inferred_complete_timeline |
| `Action_None` | 306 | 317 | 12 | inferred_complete_timeline |
| `Action_ThrowPass` | 318 | 326 | 9 | inferred_complete_timeline |
| `Action_None` | 327 | 375 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–378
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 163 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 185 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 208 | 18 | inferred_complete_timeline |
| `Action_None` | 209 | 216 | 8 | inferred_complete_timeline |
| `Action_None` | 222 | 230 | 9 | inferred_complete_timeline |
| `Action_None` | 233 | 378 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 389 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 389 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 389 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–340
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 340 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–375
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 209 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 326 | 117 | inferred_complete_timeline |
| `Action_None` | 327 | 360 | 34 | inferred_complete_timeline |
| `Action_None` | 362 | 375 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 209 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 326 | 117 | inferred_complete_timeline |
| `Action_None` | 327 | 389 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–372
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 209 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 284 | 75 | inferred_complete_timeline |
| `Action_None` | 343 | 372 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–368
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 209 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 282 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 284 | 286 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 288 | 326 | 39 | inferred_complete_timeline |
| `Action_None` | 327 | 368 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 209 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 326 | 117 | inferred_complete_timeline |
| `Action_None` | 327 | 389 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–375
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 375 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 389 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 323 | 115 | inferred_complete_timeline |
| `Action_None` | 328 | 389 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–292
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 292 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–380
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 320 | 112 | inferred_complete_timeline |
| `Action_None` | 323 | 380 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 316 | 108 | inferred_complete_timeline |
| `Action_None` | 318 | 324 | 7 | inferred_complete_timeline |
| `Action_None` | 326 | 328 | 3 | inferred_complete_timeline |
| `Action_None` | 333 | 344 | 12 | inferred_complete_timeline |
| `Action_None` | 346 | 358 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–378
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 378 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 389 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–378
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 374 | 166 | inferred_complete_timeline |
| `Action_None` | 377 | 378 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 389 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_None` | 209 | 389 | 181 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 284–337 | 25 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 293–338 | 36 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 301–383 | 83 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 342–387 | 29 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 342–343 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 345–346 | 2 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 354–389 | 31 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 369–386 | 18 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 381–387 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 117 frames exceeds threshold 90 frames [start=210, end=326].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (RT) duration 117 frames exceeds threshold 90 frames [start=210, end=326].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (LG) duration 117 frames exceeds threshold 90 frames [start=210, end=326].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (RG) duration 117 frames exceeds threshold 90 frames [start=210, end=326].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LT) duration 117 frames exceeds threshold 90 frames [start=210, end=326].
- ⚠️ Action 'Action_None' range [209-320] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-380] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-378] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-389] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-340] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-375] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-292] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-323] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-316] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-324] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-344] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-358] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-374] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [210-284] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-372] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [210-282] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [284-286] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-368] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-375] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-360] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-375] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-163] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-185] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-208] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-216] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-230] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-378] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-287] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-295] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-337] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-316] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-331] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-338] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-383] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-344] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-387] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-356] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-386] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-387] for track '30' has 1 frames without a visible bounding box.
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