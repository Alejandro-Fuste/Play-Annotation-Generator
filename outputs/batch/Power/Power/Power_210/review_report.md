# Play-Annotation-Generator Annotation Review — Power_210

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_210`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 27
- **Ball Tracks:** 2
- **Action Segments:** 60
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 1
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 47
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `12` | `12` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 9 | START | 9 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 9 | START | 9 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 9 | START | 9 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 9 | START | 9 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 9 | START | 9 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 9 | START | 9 | 307 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 9 | START | 9 | 312 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `10` | `10` | 276 | START | 276 | 301 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `12` | `12` | 276 | START | 276 | 285 |
| ✅ EXACT | `Action_DownBlock` | LT | `4` | `4` | 276 | START | 276 | 336 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `13` | `13` | 276 | START | 276 | 297 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 9–407
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 307 | 299 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 407 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 9–332
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 312 | 304 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 332 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 9–382
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 275 | 267 | inferred_complete_timeline |
| `Action_DownBlock` | 276 | 336 | 61 | inferred_complete_timeline |
| `Action_None` | 337 | 347 | 11 | inferred_complete_timeline |
| `Action_None` | 349 | 382 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 9–306
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 275 | 267 | inferred_complete_timeline |
| `Action_DownBlock` | 276 | 285 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 298 | 299 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 305 | 306 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 9–419
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 275 | 267 | inferred_complete_timeline |
| `Action_DownBlock` | 276 | 301 | 26 | inferred_complete_timeline |
| `Action_DownBlock` | 321 | 336 | 16 | inferred_complete_timeline |
| `Action_None` | 337 | 374 | 38 | inferred_complete_timeline |
| `Action_None` | 397 | 419 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 9–363
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 275 | 267 | inferred_complete_timeline |
| `Action_PullBlock` | 276 | 297 | 22 | inferred_complete_timeline |
| `Action_PullBlock` | 299 | 336 | 38 | inferred_complete_timeline |
| `Action_None` | 337 | 363 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 9–419
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 419 | 411 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 9–350
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 350 | 342 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 9–361
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 324 | 316 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 354 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 361 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 9–316
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 295 | 287 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 316 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 9–317
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 284 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 293 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 317 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 9–419
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 312 | 304 | inferred_complete_timeline |
| `Action_PreSnap` | 319 | 344 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 349 | 358 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 419 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 9–382
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 382 | 374 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 9–344
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 344 | 336 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 9–203
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 203 | 195 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `22` | Position_Unknown | Team_Unknown | 120–217 | 98 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 265–353 | 89 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 281–419 | 137 | 2 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 317–343 | 6 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 327–388 | 57 | 3 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 339–419 | 79 | 2 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 352–419 | 68 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 361–419 | 47 | 4 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 368–369 | 2 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 386–393 | 8 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 409–419 | 11 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 409–419 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | 18 | 258 | 99 | 41.1% | 21, 30, 35–37, 53–54, 56, 58–59, 81, 83, 85–90, 92–129, 131–154, 160–161, 165, 170–178, 180–189, 203–205, 220–228, 230–257 |
| `16` | `17` | 20 | 20 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 47 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [9-295] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-316] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-344] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-312] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-344] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-358] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-350] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-347] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-382] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-324] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-354] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-361] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-307] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-407] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-382] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-312] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-332] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [276-301] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-374] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-419] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-284] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-293] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-317] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [276-285] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [298-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [305-306] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [276-297] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-363] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-203] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-217] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-353] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-318] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-419] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-319] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-343] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-343] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-385] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-388] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-386] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-392] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-398] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-406] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-369] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-393] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-412] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-419] for track '28' has 2 frames without a visible bounding box.
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
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.

</details>