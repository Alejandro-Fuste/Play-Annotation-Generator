# Play-Annotation-Generator Annotation Review — Power_245

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_245`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 70
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `17` | `17` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 16 | START | 16 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 16 | START | 16 | 322 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `12` | `Group` | 16 | START | 16 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 16 | START | 16 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 16 | START | 16 | 237 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 16 | START | 16 | 276 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `19` | `Group` | 16 | START | 16 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 16 | START | 16 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 16 | START | 16 | 311 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 16 | START | 16 | 237 |
| ✅ EXACT | `Action_DownBlock` | RT | `17` | `17` | 238 | START | 238 | 273 |
| ✅ EXACT | `Action_PullBlock` | RG | `9` | `9` | 238 | START | 238 | 281 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 16–383
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 41 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 44 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 353 | 291 | inferred_complete_timeline |
| `Action_PreSnap` | 357 | 368 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 370 | 383 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 16–363
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 311 | 296 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 351 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 357 | 363 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 16–234
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 110 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 134 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 183 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 229 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 234 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 322 | 307 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 389 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 276 | 261 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 389 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 16–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 237 | 222 | inferred_complete_timeline |
| `Action_PullBlock` | 238 | 281 | 44 | inferred_complete_timeline |
| `Action_None` | 282 | 389 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 16–273
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 237 | 222 | inferred_complete_timeline |
| `Action_DownBlock` | 238 | 273 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 16–318
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 305 | 290 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 318 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 327 | 312 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 337 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 389 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 16–290
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 263 | 248 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 266 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 269 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 290 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 16–290
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 245 | 230 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 262 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 290 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 16–385
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 298 | 283 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 385 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 16–316
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 291 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 307 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 311 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 316 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 16–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 389 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 16–340
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 340 | 325 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 16–389 | 372 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 227–389 | 151 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 287–308 | 20 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 292–362 | 71 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 301–389 | 89 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 323–389 | 61 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 335–351 | 17 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 337–376 | 40 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 347–348 | 2 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 349–389 | 41 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 358–389 | 31 | 2 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 366–367 | 2 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 375–378 | 4 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 379–389 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 492: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [16-311] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-351] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-363] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-305] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-318] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-340] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-327] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-337] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-291] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-307] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-311] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-316] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-245] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-262] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-290] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-322] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-263] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-272] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-290] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-298] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-385] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-330] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-375] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-389] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [238-273] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-276] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-110] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-140] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-183] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-229] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-234] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-41] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-353] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-368] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-383] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-255] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-389] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-304] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-308] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-362] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-389] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-374] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-351] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-376] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-348] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-366] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-389] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-367] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-378] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.

</details>